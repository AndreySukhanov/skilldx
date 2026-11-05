# skillprobe report

Routing probe over 14 skills - 21 cases, 3 repeat(s) per case, 252 trials. Started 2026-11-05T14:09:42+00:00, finished 2026-11-05T14:14:14+00:00.

## Summary

| variant | pass | 95% CI | trigger precision | trigger recall | flaky cases | errors | cost | avg latency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.6-luna | 59/63 (94%) | 85-98% | - | - | 1 | 0 | $0.0143 | 2.9s |
| qwen3.8-flash | 61/63 (97%) | 89-99% | - | - | 2 | 0 | $0.0119 | 7.6s |
| deepseek-v4.1-flash | 60/63 (95%) | 87-98% | - | - | 0 | 0 | $0.0144 | 2.2s |
| glm-5.3-flash | 59/63 (94%) | 85-98% | - | - | 1 | 0 | $0.0077 | 4.2s |

Trigger precision: of the runs that loaded the target skill, how many should have. Trigger recall: of the runs that should load it, how many did. A case is flaky when its repeats disagree.

## Skill routing

Per skill and model: `loaded when required · loaded when forbidden`, by the case labels (`loads` / `not_loads`). Skills a case does not label are not scored.

| skill | gpt-5.6-luna | qwen3.8-flash | deepseek-v4.1-flash | glm-5.3-flash |
|---|---|---|---|---|
| `brainstorming` | 6/6 · 0/45 | 6/6 · 0/45 | 6/6 · 0/45 | 6/6 · 0/45 |
| `diagnosing-superpowers` | 3/3 · 0/12 | 3/3 · 0/12 | 3/3 · 0/12 | 3/3 · 0/12 |
| `dispatching-parallel-agents` | 3/3 · 0/15 | 3/3 · 0/15 | 3/3 · 0/15 | 3/3 · 0/15 |
| `executing-plans` | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 | 3/3 · 0/36 |
| `finishing-a-development-branch` | 3/3 · 0/33 | 3/3 · 0/33 | 3/3 · 0/33 | 3/3 · 0/33 |
| `receiving-code-review` | 3/3 · 0/30 | 2/3 · 0/30 | 3/3 · 0/30 | 3/3 · 0/30 |
| `requesting-code-review` | 3/3 · 0/21 | 3/3 · 0/21 | 3/3 · 0/21 | 3/3 · 0/21 |
| `subagent-driven-development` | 3/3 · 0/21 | 3/3 · 0/21 | 3/3 · 0/21 | 3/3 · 0/21 |
| `systematic-debugging` | 9/9 · 0/39 | 9/9 · 0/39 | 9/9 · 0/39 | 9/9 · 0/39 |
| `test-driven-development` | 0/3 · 0/15 | 2/3 · 0/15 | 0/3 · 0/15 | 0/3 · 0/15 |
| `using-git-worktrees` | 3/3 · 1/18 | 3/3 · 0/18 | 3/3 · 0/18 | 3/3 · 0/18 |
| `verification-before-completion` | 3/3 · 0/15 | 3/3 · 0/15 | 3/3 · 0/15 | 2/3 · 0/15 |
| `writing-plans` | 3/3 · 0/48 | 3/3 · 0/48 | 3/3 · 0/48 | 3/3 · 0/48 |
| `writing-skills` | 3/3 · 0/24 | 3/3 · 0/24 | 3/3 · 0/24 | 3/3 · 0/24 |

### Collisions

A forbidden skill loaded instead of, or next to, the expected one.

| expected | loaded | gpt-5.6-luna | qwen3.8-flash | deepseek-v4.1-flash | glm-5.3-flash |
|---|---|---|---|---|---|
| systematic-debugging | `using-git-worktrees` | 1 | 0 | 0 | 0 |

## Cases

| case | expects | gpt-5.6-luna | qwen3.8-flash | deepseek-v4.1-flash | glm-5.3-flash |
|---|---|---|---|---|---|
| `failing-test` | systematic-debugging | 2/3 | 3/3 | 3/3 | 3/3 |
| `flaky-ci` | systematic-debugging | 3/3 | 3/3 | 3/3 | 3/3 |
| `safari-export` | systematic-debugging | 3/3 | 3/3 | 3/3 | 3/3 |
| `referral-program` | brainstorming | 3/3 | 3/3 | 3/3 | 3/3 |
| `conference-talk` | brainstorming | 3/3 | 3/3 | 3/3 | 3/3 |
| `spec-to-plan` | writing-plans | 3/3 | 3/3 | 3/3 | 3/3 |
| `execute-inline` | executing-plans | 3/3 | 3/3 | 3/3 | 3/3 |
| `execute-with-subagents` | subagent-driven-development | 3/3 | 3/3 | 3/3 | 3/3 |
| `parallel-failures` | dispatching-parallel-agents | 3/3 | 3/3 | 3/3 | 3/3 |
| `receive-review` | receiving-code-review | 3/3 | 2/3 | 3/3 | 3/3 |
| `request-review` | requesting-code-review | 3/3 | 3/3 | 3/3 | 3/3 |
| `claim-done` | verification-before-completion | 3/3 | 3/3 | 3/3 | 2/3 |
| `finish-branch` | finishing-a-development-branch | 3/3 | 3/3 | 3/3 | 3/3 |
| `isolated-workspace` | using-git-worktrees | 3/3 | 3/3 | 3/3 | 3/3 |
| `iban-validator` | test-driven-development | 0/3 | 2/3 | 0/3 | 0/3 |
| `new-skill` | writing-skills | 3/3 | 3/3 | 3/3 | 3/3 |
| `diagnose-session` | diagnosing-superpowers | 3/3 | 3/3 | 3/3 | 3/3 |
| `http-418` | no skill | 3/3 | 3/3 | 3/3 | 3/3 |
| `mutex-vs-semaphore` | no skill | 3/3 | 3/3 | 3/3 | 3/3 |
| `rebase-pushed-branch` | no skill | 3/3 | 3/3 | 3/3 | 3/3 |
| `rename-variable` | no skill | 3/3 | 3/3 | 3/3 | 3/3 |

## Failures

### gpt-5.6-luna

- `failing-test` #1: not_loads (wrongly loaded=['using-git-worktrees'])
- `iban-validator` #1: loads 'test-driven-development' (loaded=['brainstorming'])
- `iban-validator` #2: loads 'test-driven-development' (loaded=['brainstorming'])
- `iban-validator` #3: loads 'test-driven-development' (loaded=['brainstorming'])

### qwen3.8-flash

- `receive-review` #2: loads 'receiving-code-review' (loaded=[])
- `iban-validator` #2: loads 'test-driven-development' (loaded=['brainstorming'])

### deepseek-v4.1-flash

- `iban-validator` #1: loads 'test-driven-development' (loaded=['brainstorming'])
- `iban-validator` #2: loads 'test-driven-development' (loaded=['brainstorming'])
- `iban-validator` #3: loads 'test-driven-development' (loaded=['brainstorming'])

### glm-5.3-flash

- `claim-done` #3: loads 'verification-before-completion' (loaded=['finishing-a-development-branch'])
- `iban-validator` #1: loads 'test-driven-development' (loaded=['brainstorming'])
- `iban-validator` #2: loads 'test-driven-development' (loaded=['brainstorming'])
- `iban-validator` #3: loads 'test-driven-development' (loaded=['brainstorming'])
