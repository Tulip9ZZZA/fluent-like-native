# Contributing

Thanks for helping improve Fluent Like Native.

## Language and lexicon changes

- Keep entries scoped to a language variety, community, domain, medium, and use case where possible.
- Include a source URL and access date for `verified-contextual` entries. Describe what the evidence does and does not establish.
- Never label wording universally native or claim community consensus from one example.
- Leave uncertain or user-supplied candidates as `draft` or `needs-review`.
- Avoid private messages, closed communities, personal data, and long copyrighted excerpts. Short examples should be permissioned or otherwise appropriate to redistribute.
- Explain sensitive, derogatory, dated, or potentially harmful wording in `caution`.

## Checks

Run:

```bash
python3 skills/fluent-like-native/scripts/lexicon.py validate skills/fluent-like-native/references/lexicon.csv
git diff --check
```

Keep `SKILL.md` focused on the core workflow. Move detailed procedures and examples into references so agents can load them only when relevant.
