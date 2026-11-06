# skilldx report

Routing probe over 14 skills - 25 cases, 3 repeat(s) per case, 375 trials. Started 2026-11-05T13:32:21+00:00, finished 2026-11-05T14:07:28+00:00.

## Summary

| variant | pass | 95% CI | trigger precision | trigger recall | flaky cases | errors | cost | avg latency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.6-luna | 72/75 (96%) | 89-99% | - | - | 0 | 0 | $0.0110 | 3.1s |
| qwen3.8-flash | 74/75 (99%) | 93-100% | - | - | 1 | 0 | $0.0178 | 10.4s |
| deepseek-v4.1-flash | 75/75 (100%) | 95-100% | - | - | 0 | 0 | $0.0262 | 2.6s |
| glm-5.3-flash | 75/75 (100%) | 95-100% | - | - | 0 | 0 | $0.0167 | 3.7s |
| kimi-k3 | 74/75 (99%) | 93-100% | - | - | 1 | 0 | $2.28 | 29.0s |

Trigger precision: of the runs that loaded the target skill, how many should have. Trigger recall: of the runs that should load it, how many did. A case is flaky when its repeats disagree.

## Skill routing

Per skill and model: `loaded when required · loaded when forbidden`, by the case labels (`loads` / `not_loads`). Skills a case does not label are not scored.

| skill | gpt-5.6-luna | qwen3.8-flash | deepseek-v4.1-flash | glm-5.3-flash | kimi-k3 |
|---|---|---|---|---|---|
| `academy-guide` | 3/3 · 3/48 | 3/3 · 0/48 | 3/3 · 0/48 | 3/3 · 0/48 | 3/3 · 0/48 |
| `algorithmic-art` | 3/3 · 0/30 | 3/3 · 0/30 | 3/3 · 0/30 | 3/3 · 0/30 | 3/3 · 0/30 |
| `brand-guidelines` | 3/3 · 0/24 | 3/3 · 0/24 | 3/3 · 0/24 | 3/3 · 0/24 | 3/3 · 0/24 |
| `canvas-design` | 6/6 · 0/51 | 6/6 · 0/51 | 6/6 · 0/51 | 6/6 · 0/51 | 6/6 · 0/51 |
| `claude-api` | 3/3 · 0/18 | 3/3 · 1/18 | 3/3 · 0/18 | 3/3 · 0/18 | 3/3 · 0/18 |
| `discernment-nudge` | - · 0/21 | - · 0/21 | - · 0/21 | - · 0/21 | - · 0/21 |
| `frontend-design` | 3/3 · 0/27 | 3/3 · 0/27 | 3/3 · 0/27 | 3/3 · 0/27 | 3/3 · 0/27 |
| `internal-comms` | 6/6 · 0/27 | 6/6 · 0/27 | 6/6 · 0/27 | 6/6 · 0/27 | 6/6 · 0/27 |
| `mcp-builder` | 3/3 · 0/42 | 3/3 · 0/42 | 3/3 · 0/42 | 3/3 · 0/42 | 3/3 · 1/42 |
| `skill-creator` | 6/6 · 0/30 | 6/6 · 0/30 | 6/6 · 0/30 | 6/6 · 0/30 | 6/6 · 0/30 |
| `slack-gif-creator` | 3/3 · 0/27 | 3/3 · 0/27 | 3/3 · 0/27 | 3/3 · 0/27 | 3/3 · 0/27 |
| `theme-factory` | 3/3 · 0/18 | 3/3 · 0/18 | 3/3 · 0/18 | 3/3 · 0/18 | 3/3 · 0/18 |
| `web-artifacts-builder` | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 |
| `webapp-testing` | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 |

### Collisions

A forbidden skill loaded instead of, or next to, the expected one.

| expected | loaded | gpt-5.6-luna | qwen3.8-flash | deepseek-v4.1-flash | glm-5.3-flash | kimi-k3 |
|---|---|---|---|---|---|---|
| mcp-builder | `academy-guide` | 3 | 0 | 0 | 0 | 0 |
| no skill | `claude-api` | 0 | 1 | 0 | 0 | 0 |
| no skill | `mcp-builder` | 0 | 0 | 0 | 0 | 1 |

## Cases

| case | expects | gpt-5.6-luna | qwen3.8-flash | deepseek-v4.1-flash | glm-5.3-flash | kimi-k3 |
|---|---|---|---|---|---|---|
| `art-flow-field` | algorithmic-art | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `poster-print` | canvas-design | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `wall-print` | canvas-design | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `slack-gif` | slack-gif-creator | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `frames-to-mp4` | no skill | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `landing-aesthetic` | frontend-design | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `react-artifact` | web-artifacts-builder | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `single-html-toggle` | - | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `playwright-login` | webapp-testing | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `pytest-unit` | no skill | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `mcp-jira` | mcp-builder | 0/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `mcp-explain` | - | 3/3 | 3/3 | 3/3 | 3/3 | 2/3 |
| `skill-description-fix` | skill-creator | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `skill-evals` | skill-creator | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `leadership-update` | internal-comms | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `incident-report` | internal-comms | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `cold-email` | - | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `anthropic-brand` | brand-guidelines | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `preset-theme` | theme-factory | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `claude-pricing` | claude-api | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `openai-streaming` | - | 3/3 | 2/3 | 3/3 | 3/3 | 3/3 |
| `academy-start` | academy-guide | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `capital-city` | no skill | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `translate-greeting` | no skill | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| `rename-jpeg` | no skill | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |

## Failures

### gpt-5.6-luna

- `mcp-jira` #1: not_loads (wrongly loaded=['academy-guide'])
- `mcp-jira` #2: not_loads (wrongly loaded=['academy-guide'])
- `mcp-jira` #3: not_loads (wrongly loaded=['academy-guide'])

### qwen3.8-flash

- `openai-streaming` #3: not_loads (wrongly loaded=['claude-api'])

### kimi-k3

- `mcp-explain` #1: not_loads (wrongly loaded=['mcp-builder'])
