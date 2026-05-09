# SKILL-SPEC Closing Checklist

Every skill must pass all items before delivery. Check each box or fix the issue.

## Frontmatter

- [ ] `name` present and explicit (not relying on runtime defaults)
- [ ] `name` is lowercase + hyphens only, max 64 chars
- [ ] `name` matches the skill's actual job, no generic big words
- [ ] `description` present and explicit
- [ ] `description` max 1024 chars
- [ ] `description` first 250 chars contain key trigger words
- [ ] `description` answers: what / when to use / when NOT to use
- [ ] No XML tags or format control chars in frontmatter
- [ ] All frontmatter fields are supported by current runtime

## SKILL.md Structure

- [ ] Has all 8 required sections in order: Purpose, When to use, When NOT to use, Inputs/Preconditions, Workflow, Outputs, Error handling, Resources
- [ ] Total line count under 500
- [ ] Purpose is 1 sentence to 1 short paragraph (no long background)
- [ ] "When to use" lists real trigger scenarios, not abstract capabilities
- [ ] "When NOT to use" lists near-miss scenarios
- [ ] Inputs/Preconditions specifies how to get missing info
- [ ] Outputs specifies exact deliverable structure/format

## Workflow Quality

- [ ] Uses numbered steps
- [ ] Steps are in real execution order (setup → decide → execute → validate → output)
- [ ] Every step is an action, not a topic word
- [ ] Each step says what you get after completing it
- [ ] Blocking steps marked BLOCKING
- [ ] Confirmation-required steps marked CONFIRM
- [ ] Conditional steps marked CONDITIONAL with trigger conditions
- [ ] Default path written first, branches after
- [ ] High-cost / irreversible / preference-sensitive ops have explicit confirm nodes
- [ ] Output-producing skills have a pre-delivery quality check

## Directory Structure

- [ ] `SKILL.md` exists at root
- [ ] No `README.md`, `CHANGELOG.md`, `INSTALLATION_GUIDE.md`, or `QUICK_REFERENCE.md`
- [ ] No top-level `templates/` or `examples/` directories
- [ ] Long rules/docs in `references/`, not in SKILL.md body
- [ ] Mechanical/repeatable steps in `scripts/`, not described inline
- [ ] Reusable templates in `assets/templates/`
- [ ] Every file in subdirectories is referenced by name in SKILL.md §Resources

## Progressive Disclosure

- [ ] Frontmatter only handles triggering and boundaries
- [ ] SKILL.md only handles default execution path
- [ ] Detail/reference material is in subdirectories, loaded on demand
- [ ] No long templates pasted inline in SKILL.md
- [ ] No scriptable steps left as prose for the model to re-derive

## Evals (required for team-shared skills)

- [ ] `evals/evals.json` exists
- [ ] At least 2 should-trigger prompts
- [ ] At least 2 should-not-trigger / near-miss prompts
- [ ] At least 1 core-function eval with expected output
- [ ] Eval prompts are realistic, not synthetic

## Gotchas (if present)

- [ ] Each gotcha has: Title, Trigger, Symptom, Wrong handling, Correct handling, Test backfill, Version/Notes
- [ ] Each gotcha has a clear trigger condition and correct resolution
- [ ] No vague complaints, personal preferences, or experience journals
