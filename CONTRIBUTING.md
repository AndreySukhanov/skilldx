# Contributing to skilldx

Thanks for your interest! Contributions are welcome. The most valuable additions are small and self-contained.

## Great first contributions

### 1. A golden set for a public skill collection
Probes live in `examples/`. A routing probe is a folder with the skills (frontmatter is enough for `routing_only`), a `cases.yaml` and a `probe.yaml` - see `examples/public-skills/anthropic/` for a complete one.

- Label by the rules in [`examples/public-skills/LABELS.md`](examples/public-skills/LABELS.md): `loads` is the skill whose own description names the request, `not_loads` lists skills that clearly do not apply, everything else stays unlabeled.
- Record the source commit and the license of every copied skill in a `SOURCES.md`, and keep the original license file next to them.
- Commit the report and `results.json`, not the response cache.

### 2. A provider preset
Providers are OpenAI-compatible base URLs plus the name of the environment variable holding the key (`skilldx/config.py`). A new preset is a few lines - link the vendor's documentation for its OpenAI-compatible API in the PR.

### 3. A new deterministic check
Checks live in `skilldx/checks.py`; the `expect` schema is in `skilldx/cases.py`. Add the field, the check, and a test with the scripted fake client.

## Development setup

```bash
pip install -e ".[dev]"
pytest
```

Tests use a scripted fake client - no network, no keys. CI runs them on Python 3.10 and 3.13.

## Ground rules

- **English everywhere** - code, comments, commits, PRs.
- Every new feature comes with a test that runs offline.
- Numbers in the README come from a committed report. If you rerun a probe, commit the new `results/` together with the README change.

## Bigger changes

Open an issue first and describe the approach - happy to discuss the design before you invest time.

## License

By contributing you agree that your contribution is licensed under the project's [LICENSE](LICENSE).
