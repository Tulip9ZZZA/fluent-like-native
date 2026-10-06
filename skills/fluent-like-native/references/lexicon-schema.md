# Lexicon schema

`lexicon.csv` is UTF-8 CSV. Keep one row per sense or context; repeat a term when it has different meanings, registers, or regions. Empty optional fields are preferable to invented details.

| Column | Required | Meaning |
| --- | --- | --- |
| `language` | yes | BCP-47 style tag when known (for example, `th-TH`, `es-MX`). |
| `term` | yes | Exact form in the original writing system. |
| `transliteration` | no | Readable phonetic aid; identify the scheme in `notes` if needed. |
| `gloss` | yes | Short meaning in the project's working language. |
| `function` | yes | What the expression does in conversation, beyond dictionary meaning. |
| `domain` | yes | Topic or community scope. |
| `locale` | yes | Country, region, community, or `unspecified`. |
| `register` | yes | Examples: formal, neutral, casual, slang, technical. |
| `medium` | yes | Examples: speech, chat, caption, workplace. |
| `audience` | no | Audience for which the evidence is relevant. |
| `example` | no | Short original-language example, not copied at length. |
| `caution` | no | Ambiguity, sensitivity, datedness, social risk, or “avoid” condition. |
| `source_url` | no | Public URL, or blank for a draft/user-supplied candidate. |
| `source_date` | no | Source publication date in ISO format if visible; otherwise blank. |
| `accessed_at` | no | Research access date in ISO format; blank until checked. |
| `confidence` | yes | `low`, `medium`, or `high`, with limits explained in `notes`. |
| `status` | yes | `draft`, `needs-review`, `verified-contextual`, or `retired`. |
| `notes` | no | Provenance, scope, verification method, or unresolved questions. |

## Confidence and status

- **low**: unverified suggestion, single weak example, or uncertain interpretation.
- **medium**: more than one relevant example, with context still limited or mixed.
- **high**: strong, context-matched evidence from suitable sources; still not universal.
- `verified-contextual` means the cited evidence was checked for the stated scope. It does not mean “universally native.”
- A verified row must include `source_url` and `accessed_at`. Lower-confidence rows may be useful as leads, but the skill must not present them as verified.
- Set `retired` when stale or contradicted; retain the reason in `notes` instead of silently deleting history.
