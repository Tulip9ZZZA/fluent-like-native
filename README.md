# Fluent Like Native

<p align="center"><img src="assets/logo.svg" alt="Fluent Like Native logo: a white flowing F inside a coral speech bubble" width="112"></p>

**A context-aware writing skill for natural, culturally aware language.**

Fluent Like Native helps an AI agent write, translate, adapt, and review language for a specific audience and situation. It combines a practical linguistic workflow with optional, source-traceable vocabulary research. It is designed for social content, professional communication, public speaking, customer support, learning materials, and other user-defined contexts.

> “Like native” describes the goal of natural, context-appropriate communication. It is not a claim that generated text is indistinguishable from every native speaker, region, or community.

## What it does

- Identifies the requested language, locale, audience, medium, relationship, tone, and outcome.
- Chooses register, idiom, honorifics, pronouns, politeness, code-switching, and level of directness for that context.
- Preserves meaning and intent instead of translating word for word.
- Looks up niche terminology and current slang when research tools are available and the task needs it.
- Tracks vocabulary with context, evidence, source, date, confidence, and usage cautions in plain CSV.
- Supports a user-maintained lexicon when live research is unavailable or not wanted.
- Flags uncertainty and offers alternatives when a phrase is regional, dated, sensitive, or disputed.

Its **FORGE** workflow is: **Frame** the communication brief, **Observe** relevant evidence, **Register** the voice, **Generate** the language, then **Examine** meaning and fit before delivery.

## Repository layout

```text
fluent-like-native/
├── README.md
├── assets/
│   ├── logo.svg
│   └── examples/
│       ├── thai-fitness-baseline.png
│       └── thai-fitness-with-skill.png
├── LICENSE
├── CONTRIBUTING.md
├── .github/workflows/validate.yml
├── .gitignore
├── skills/
│   └── fluent-like-native/
│       ├── SKILL.md
│       ├── references/
│       │   ├── lexicon-schema.md
│       │   ├── research-playbook.md
│       │   ├── style-decisions.md
│       │   └── lexicon.csv
│       ├── scripts/
│       │   └── lexicon.py
│       └── assets/
│           └── research-brief-template.md
└── examples/
    └── requests.md
```

The skill follows the open Agent Skills folder format. Its core instructions stay short; detailed procedures and the lexicon load only when relevant.

## Install

Copy `skills/fluent-like-native/` into the skills directory supported by your agent. For clients that support project-level Agent Skills, one common location is:

```text
.agents/skills/fluent-like-native/
```

Other clients may use a different skills directory. Keep the folder name `fluent-like-native` so it matches the `name` in `SKILL.md`.

## Use it

Ask for the result you need and supply whatever context you know. The agent should ask only for details that materially change the language choice; otherwise it should state a sensible assumption and proceed.

```text
Use Fluent Like Native. Write 3 Thai TikTok caption options for beginner lifters
in Bangkok. Audience: 18–25. Goal: encourage consistency without body shaming.
Tone: energetic, friendly, credible. Keep each under 100 characters.
Research current niche slang if useful and cite the sources you rely on.
```

```text
Use Fluent Like Native. Rewrite this customer-support reply in Mexican Spanish.
The customer is frustrated; be warm and accountable, but do not promise a refund.
Explain your choices briefly after the final reply.
```

```text
Use Fluent Like Native. Review this speech in English for a Thai audience.
Keep the meaning, make it sound natural when spoken, and mark any claim that
needs a human cultural review: [paste draft]
```

## Thai fitness example

The repository includes the two user-provided Thai fitness screenshots as an illustrative before/with-skill comparison. The first shows the brief without an explicit skill call; the second includes `/fluent-like-native`. They demonstrate an example workflow, not a controlled language-quality evaluation. The fitness claims in the images have not been medically or scientifically reviewed; verify them with qualified sources before reuse.

| Baseline prompt | Prompt invoking the skill |
| --- | --- |
| [View the baseline example](assets/examples/thai-fitness-baseline.png) | [View the skill example](assets/examples/thai-fitness-with-skill.png) |

## On-demand research

When a task depends on niche, fast-changing, or locally specific language, the skill directs the agent to research actual usage if a web search or browsing tool is available. It compares multiple independent examples, prefers primary community or institutional sources where appropriate, distinguishes observed wording from the agent's interpretation, and records URLs and access dates. It does not scrape private groups, infer demographic identity, or treat a single viral post as universal usage.

If no research tool is available, it uses the supplied CSV, asks the user for a source, or labels suggestions as provisional. It never fabricates citations. See [`research-playbook.md`](skills/fluent-like-native/references/research-playbook.md).

## Bring your own vocabulary

Edit `skills/fluent-like-native/references/lexicon.csv` in any spreadsheet editor. Keep one meaning or use-case per row. Use `draft` or `needs-review` until evidence supports stronger wording. The schema and confidence labels are documented in [`lexicon-schema.md`](skills/fluent-like-native/references/lexicon-schema.md).

Search the CSV from the command line (Python 3, no third-party packages):

```bash
python3 skills/fluent-like-native/scripts/lexicon.py search \
  skills/fluent-like-native/references/lexicon.csv --query "ขอสลับเล่น"

python3 skills/fluent-like-native/scripts/lexicon.py validate \
  skills/fluent-like-native/references/lexicon.csv
```

A checked CSV is a retrieval aid, not proof that every entry remains current or fits every speaker.

## Quality principles

1. **Context before slang.** Natural language is not a pile of trendy phrases.
2. **Intent before literal form.** Keep the source meaning, relevant facts, and requested outcome.
3. **Specificity without stereotyping.** Do not assume one voice represents a whole language community.
4. **Evidence with limits.** A source supports the context it shows, not universal frequency or acceptance.
5. **Choices when context varies.** Give register-appropriate alternatives instead of forcing one “native” answer.
6. **Human review for high-impact text.** Escalate legal, medical, safety, religious, public-policy, or crisis language to qualified review.

## Contributing

Contributions should add useful, contextualized language evidence—not undifferentiated word lists. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting changes.

## License

MIT. See [`LICENSE`](LICENSE).

## Format reference

This repository uses the [Agent Skills specification](https://agentskills.io/specification) and its [skill-creation best practices](https://agentskills.io/skill-creation/best-practices). The skill is model- and provider-neutral; actual search and file-reading capabilities depend on the agent client.
