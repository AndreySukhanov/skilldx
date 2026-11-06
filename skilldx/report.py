"""Markdown report and JSON dump of a probe run."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .engine import ProbeRun, VariantSummary


def _pct(value: float | None) -> str:
    return "-" if value is None else f"{value * 100:.0f}%"


def _money(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"${value:.4f}" if value < 1 else f"${value:.2f}"


def summary_table(run: ProbeRun) -> str:
    rows = [
        "| variant | pass | 95% CI | trigger precision | trigger recall | flaky cases | errors | cost | avg latency |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for variant in run.variants:
        s: VariantSummary = run.summary(variant)
        lo, hi = s.interval
        not_run = f", {s.skipped} not run" if s.skipped else ""
        rows.append(
            f"| {s.name} | {s.passed}/{s.total} ({_pct(s.pass_rate)}{not_run}) | {lo * 100:.0f}-{hi * 100:.0f}% "
            f"| {_pct(s.trigger_precision)} | {_pct(s.trigger_recall)} | {len(s.flaky_cases)} "
            f"| {s.errors} | {_money(s.cost_usd)} "
            f"| {'-' if s.avg_latency_s is None else f'{s.avg_latency_s:.1f}s'} |"
        )
    return "\n".join(rows)


def _ratio_cell(num: int, den: int) -> str:
    return f"{num}/{den}" if den else "-"


def routing_section(run: ProbeRun) -> list[str]:
    variants = [v for v in run.variants if v.with_skills]
    if not run.is_routing or not variants:
        return []
    per_variant = {v.name: {r.skill: r for r in run.routing(v)} for v in variants}
    skills = [s.name for s in variants[0].skills]
    lines = [
        "## Skill routing",
        "",
        "Per skill and model: `loaded when required · loaded when forbidden`, by the case labels "
        "(`loads` / `not_loads`). Skills a case does not label are not scored.",
        "",
        "| skill | " + " | ".join(v.name for v in variants) + " |",
        "|---|" + "---|" * len(variants),
    ]
    for skill in skills:
        cells = []
        for v in variants:
            r = per_variant[v.name][skill]
            cells.append(
                f"{_ratio_cell(r.loaded_when_required, r.required)} · "
                f"{_ratio_cell(r.loaded_when_forbidden, r.forbidden)}"
            )
        lines.append(f"| `{skill}` | " + " | ".join(cells) + " |")

    collisions = {v.name: run.collisions(v) for v in variants}
    keys = sorted(
        {k for c in collisions.values() for k in c},
        key=lambda k: (-sum(c.get(k, 0) for c in collisions.values()), k),
    )
    lines += ["", "### Collisions", "", "A forbidden skill loaded instead of, or next to, the expected one.", ""]
    if not keys:
        lines.append("None.")
    else:
        lines += [
            "| expected | loaded | " + " | ".join(v.name for v in variants) + " |",
            "|---|---|" + "---|" * len(variants),
        ]
        for expected, loaded in keys:
            cells = [str(collisions[v.name].get((expected, loaded), 0)) for v in variants]
            lines.append(f"| {expected} | `{loaded}` | " + " | ".join(cells) + " |")
    return lines + [""]


def _expects(case) -> str:
    e = case.expect
    if e.triggered is not None:
        return "yes" if e.triggered else "no"
    if e.loads:
        return ", ".join(e.loads)
    if "*" in e.not_loads:
        return "no skill"
    return "-"


def render_markdown(run: ProbeRun, *, output_chars: int = 240) -> str:
    total_trials = len(run.trials)
    offered = len(run.variants[0].skills) if run.variants else 0
    subject = f"Routing probe over {offered} skills" if run.is_routing else f"Target skill: `{run.target}`"
    lines = [
        "# skilldx report",
        "",
        f"{subject} - {len(run.cases)} cases, {run.repeats} repeat(s) per case, "
        f"{total_trials} trials. Started {run.started_at}, finished {run.finished_at}.",
        "",
        "## Summary",
        "",
        summary_table(run),
        "",
        "Trigger precision: of the runs that loaded the target skill, how many should have. "
        "Trigger recall: of the runs that should load it, how many did. A case is flaky when its repeats disagree.",
        "",
        *routing_section(run),
        "## Cases",
        "",
        "| case | expects | " + " | ".join(v.name for v in run.variants) + " |",
        "|---|---|" + "---|" * len(run.variants),
    ]
    for case in run.cases:
        cells = []
        for variant in run.variants:
            trials = [t for t in run.trials_for(variant.name, case.id) if not t.skipped]
            cells.append(f"{sum(t.passed for t in trials)}/{len(trials)}" if trials else "-")
        lines.append(f"| `{case.id}` | {_expects(case)} | " + " | ".join(cells) + " |")

    failures = [t for t in run.trials if not t.passed and not t.skipped]
    lines += ["", "## Failures", ""]
    if not failures:
        lines.append("None.")
    for variant in run.variants:
        vf = [t for t in failures if t.variant == variant.name]
        if not vf:
            continue
        lines += [f"### {variant.name}", ""]
        for t in vf:
            if t.result.error:
                reason = f"error: {t.result.error}"
            else:
                reason = "; ".join(
                    c.name + (f" ({c.detail})" if c.detail else "") for c in t.checks if not c.passed
                )
            snippet = " ".join(t.result.output.split())[:output_chars]
            lines.append(f"- `{t.case_id}` #{t.repeat + 1}: {reason}")
            if snippet:
                lines.append(f"  > {snippet}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def to_json(run: ProbeRun) -> str:
    data: dict[str, Any] = {
        "target": run.target,
        "repeats": run.repeats,
        "started_at": run.started_at,
        "finished_at": run.finished_at,
        "cases": [c.model_dump(exclude={"files"}) | {"files": [Path(f).name for f in c.files]} for c in run.cases],
        "variants": [
            {"name": v.name, "model": v.spec.model, "provider": v.spec.provider, "skills": [s.name for s in v.skills]}
            for v in run.variants
        ],
        "summary": [asdict(run.summary(v)) for v in run.variants],
        "routing": (
            {v.name: [asdict(r) for r in run.routing(v)] for v in run.variants if v.with_skills}
            if run.is_routing
            else {}
        ),
        "trials": [
            {
                "variant": t.variant,
                "case_id": t.case_id,
                "repeat": t.repeat,
                "passed": t.passed,
                "skipped": t.skipped,
                "checks": [asdict(c) for c in t.checks],
                "result": asdict(t.result),
            }
            for t in run.trials
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
