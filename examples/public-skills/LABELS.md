# How the golden sets are labeled

Each case is a realistic user request with routing labels, written before any model was run.

- **`loads`** - the skill whose own description names this kind of request. One per case.
- **`not_loads`** - skills that must stay unloaded: their description excludes the request
  (for example `web-artifacts-builder` says "not for simple single-file HTML"), or the request clearly
  belongs to another skill's stated domain. `"*"` - no skill applies at all.
- **Not labeled** - skills that could reasonably load next to the expected one. They are not scored,
  so a model is not punished for a defensible co-load. Superpowers skills are designed to stack,
  so its cases forbid less than the Anthropic set does.
- **Ambiguous requests are dropped**, not forced into a label. Example: "review my teammate's pull request"
  fits neither `requesting-code-review` (your own work) nor `receiving-code-review` (feedback you got)
  cleanly, so it is not in the set.

Case types (`tags`): `positive` - one skill should load; `near-miss` - close to a skill's domain but outside it;
`none` - plain questions where no skill applies.

Limits: one labeler, 25 + 21 cases, first-turn routing only (a model that loads a second skill after reading
the first one's body is not measured). Disagree with a label? Change it in `cases.yaml` and rebuild the report
from the cache with `--cache-only` - no API calls.
