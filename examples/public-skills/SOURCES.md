# Sources

Both probes use real, public skills. Only each skill's YAML frontmatter (`name`, `description` and any other
frontmatter fields) is copied, unchanged; the body is replaced with a one-line stub. A routing probe
(`routing_only: true`) never sends bodies to the model, so the model sees exactly what it would see in a
real agent: the list of names and descriptions.

| probe | source | commit | skills | license |
|---|---|---|---|---|
| `anthropic/` | [anthropics/skills](https://github.com/anthropics/skills) | `ca45fc496a3436251f191354091d557da31c15b5` | 14 of the skills under `skills/` that ship an Apache-2.0 `LICENSE.txt`; `doc-coauthoring` (no license file) and the document skills (`docx`, `pdf`, `pptx`, `xlsx`) are left out | Apache-2.0, see [`anthropic/LICENSE-Apache-2.0.txt`](anthropic/LICENSE-Apache-2.0.txt) |
| `superpowers/` | [obra/superpowers](https://github.com/obra/superpowers) | `22f0b463e7a5e579904dd6211a520321035526f7` | all 15 skills except `using-superpowers`, which the plugin injects at session start instead of routing it | MIT, see [`superpowers/LICENSE-MIT`](superpowers/LICENSE-MIT) |

Modification notice (Apache-2.0, section 4b): skill bodies were removed; frontmatter is verbatim.
