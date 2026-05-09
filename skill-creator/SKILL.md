---
name: skill-creator
description: Create new Claude Code skills that conform to SKILL-SPEC standards. Use when creating a new skill, converting an ad-hoc workflow into a skill, or auditing/fixing an existing skill's structure. Not for one-off scripts, not for editing skill content without structural changes. TRIGGER ON "create skill", "new skill", "make a skill", "skill from", "audit skill".
---

# Skill Creator

## Purpose

Generate skills that strictly conform to the SKILL-SPEC standard. Every skill produced must pass the closing checklist before delivery.

## When to use me

- User asks to create a new skill
- User wants to convert a repeated workflow into a reusable skill
- User asks to audit or restructure an existing skill against the SPEC

## When NOT to use me

- One-off scripts or automations that won't be reused
- Editing existing skill content (logic/wording) without structural changes
- Creating non-skill automation (hooks, cron jobs, config changes)

## Inputs / Preconditions

Required:
- **What the skill does** — a clear description of the task it automates
- **When it triggers** — real user prompts or scenarios that should invoke it
- **When it should NOT trigger** — near-miss scenarios

Optional (will be asked if missing):
- Example inputs/outputs
- Known gotchas or failure modes
- Scripts that should be bundled

If the user provides only a vague idea, run a brief interview (max 5 questions) to nail down the 3 required inputs before generating anything.

## Workflow

### 1. Gather requirements — BLOCKING

Confirm these 3 items before proceeding:
- What does it do (one sentence)
- Real trigger scenarios (2+)
- Near-miss / not-for scenarios (2+)

If any are missing, ask the user. Do not proceed without all three.

### 2. Draft frontmatter

Write `name` and `description` following these rules:
- `name`: lowercase + hyphens only, max 64 chars, matches the skill's job
- `description`: max 1024 chars; first 250 chars must contain the key trigger words; must answer what/when/not-when; end with `TRIGGER ON <keywords>`

Validate against `references/spec-checklist.md` §Frontmatter.

### 3. Draft SKILL.md structure

Use the template at `assets/templates/SKILL-template.md`. Fill all 8 required sections:
1. Purpose (1 sentence to 1 short paragraph)
2. When to use me (real trigger scenarios, not abstract capabilities)
3. When NOT to use me (near-miss scenarios)
4. Inputs / Preconditions (what's needed, how to get missing info)
5. Workflow (numbered steps, action verbs, BLOCKING/CONFIRM/CONDITIONAL markers)
6. Outputs (exact deliverables and format)
7. Error handling / Fallback (what to do when preconditions fail)
8. Resources (explicit references to every file in subdirectories)

Rules:
- SKILL.md must stay under 500 lines
- Workflow steps must be actions, not topic words
- Default path first, then branches
- Imperative voice throughout

### 4. Decide directory structure

Minimum:
```
skill-name/
└── SKILL.md
```

Add directories only when needed:
- `references/` — if any rule/example/doc is too long for SKILL.md body
- `scripts/` — if any step is stable, mechanical, and error-prone
- `assets/templates/` — if the skill produces files from a reusable template
- `evals/` — always create for team-shared skills
- `gotchas/` — if there are known high-cost, reproducible failure patterns

### 5. Generate files

Create all files. For each subdirectory file, ensure SKILL.md §Resources references it by name.

### 6. Generate evals — CONDITIONAL (skip for personal-only skills)

Create `evals/evals.json` with at minimum:
- 2 should-trigger prompts
- 2 should-not-trigger / near-miss prompts
- 1 core-function eval with expected output description

### 7. Run closing checklist — BLOCKING

Walk through every item in `references/spec-checklist.md`. If any item fails, fix it before delivery. Report the checklist result to the user.

### 8. Output to user

Present:
- Directory tree of the created skill
- The full SKILL.md content for review
- Checklist pass/fail summary
- Any items that need user decision

## Outputs

- A complete skill directory under `/root/.claude/skills/<skill-name>/`
- All files conforming to SKILL-SPEC
- A passing closing checklist

## Error handling / Fallback

- **User can't articulate triggers**: Offer 3 example prompts and ask "would this invoke the skill?"
- **Skill scope too broad**: Suggest splitting into 2+ focused skills
- **SKILL.md exceeds 500 lines**: Move long content to `references/`, long templates to `assets/templates/`, mechanical steps to `scripts/`
- **Existing skill conflicts**: Show the conflict and ask user how to resolve

## Resources

- `references/spec-checklist.md` — The complete closing checklist, extracted from SKILL-SPEC §8.3 and §7
- `assets/templates/SKILL-template.md` — Skeleton SKILL.md with all 8 required sections
- `evals/evals.json` — Self-eval for the skill-creator itself
