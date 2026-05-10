---
name: wiki-kb
description: Maintain an LLM-managed personal knowledge base following the LLM Wiki pattern. Ingest raw sources into a structured Obsidian wiki, query the wiki with citations, and lint for quality. Use when ingesting articles, searching the wiki, or health-checking the wiki. Not for general coding, one-off web searches, or editing raw/ sources. TRIGGER ON "ingest", "wiki", "lint wiki", "search wiki", "add to wiki", "process article", "file into wiki"
---

# Wiki KB

## Purpose

Maintain a persistent, interlinked Obsidian knowledge base where the LLM does all the writing, cross-referencing, and bookkeeping. Follows the LLM Wiki pattern: raw sources are immutable, the wiki is LLM-owned, and knowledge compounds over time.

## When to use me

- User drops an article/document into `wiki-kb/raw/` and says "ingest this" / "process this" / "add this to wiki"
- User asks "what does the wiki say about X" / "search wiki for X" / "查wiki"
- User says "lint the wiki" / "health check wiki" / "检查wiki"
- User says "file this into wiki" / "把这段存进wiki" after a discussion
- User opens a file in `wiki-kb/raw/` and asks to process it

## When NOT to use me

- General coding, debugging, or refactoring tasks
- One-off web searches unrelated to the wiki ("search the web for X")
- Editing files directly in `wiki-kb/raw/` (raw sources are immutable)
- Creating Claude Code skills, hooks, or config
- Questions asked against code or project docs, not the wiki
- Operating on files outside the `wiki-kb/` directory

## Inputs / Preconditions

Required:
- For **ingest**: a source file exists in `wiki-kb/raw/` or user provides a URL to clip
- For **query**: user asks a question about topics covered in the wiki
- For **lint**: the wiki has existing pages to check

Optional:
- User may specify emphasis (e.g., "focus on the security implications")
- User may request a specific output format (markdown page, comparison table, Marp slides, chart)

If missing: ask user which source file to ingest, or what topic to query.

## Workflow

### Determine operation — BLOCKING

Parse user intent into one of three modes:
- **Ingest** → steps 1-9 below
- **Query** → steps Q1-Q4 below
- **Lint** → steps L1-L4 below

---

## Ingest (default path)

### 1. Identify source file(s) — BLOCKING

Read `wiki-kb/raw/` listing. Match user's reference to file(s). If user mentions a URL not yet in raw/, suggest clipping it first.

Result: confirmed file path(s) in raw/.

### 2. Read source and extract — BLOCKING

Read the full source. Extract:
- Main thesis / argument
- Key entities (people, orgs, products, projects)
- Key concepts (frameworks, terms, ideas)
- Notable claims or data points
- Contradictions with existing wiki pages (if any)

Result: structured notes ready for user discussion.

### 3. Discuss takeaways with user — CONFIRM

Present a brief summary of what was found and the 3-5 most important points. Ask:
- What to emphasize or de-emphasize
- Any specific angle the user cares about
- Whether to batch-process or discuss in detail

Result: user-confirmed direction for wiki updates.

### 4. Create/update source summary page — BLOCKING

Create `wiki-kb/wiki/sources/<source-name>.md` using the template at `assets/templates/source-page.md`.

Must include:
- YAML frontmatter (title, source URL, author, date, tags)
- One-paragraph summary
- Key takeaways (bullet list)
- Links to mentioned entities and concepts via `[[wikilinks]]`

Result: source page filed.

### 5. Update entity pages — CONDITIONAL (skip if no new entities)

For each person, org, product, or project mentioned:
- Create `wiki-kb/wiki/entities/<name>.md` if new
- Append a "Mentioned in" section linking back to the source page
- Update the entity's summary if new information changes the picture

Result: entity pages created or updated with backlinks.

### 6. Update concept pages — CONDITIONAL (skip if no new concepts)

For each framework, term, or idea explained:
- Create `wiki-kb/wiki/concepts/<concept>.md` if new
- Append a "Referenced in" section linking to the source page
- If multiple sources discuss the same concept, synthesize a coherent definition with citations

Result: concept pages created or updated with backlinks.

### 7. Create analysis pages — CONDITIONAL (skip if nothing to synthesize)

When the source bridges multiple entities/concepts or presents a novel argument:
- Create `wiki-kb/wiki/analyses/<topic>.md`
- Cross-reference entities and concepts with `[[wikilinks]]`
- Note contradictions with prior sources if relevant

Result: analysis page filed.

### 8. Update macro pages — CONDITIONAL (skip for niche sources)

Update `wiki-kb/wiki/macro/` overview pages if the source shifts the big picture:
- Topic overviews
- Synthesis or thesis pages
- Comparison tables

Result: macro pages updated.

### 9. Update index and log — BLOCKING

Append to `wiki-kb/wiki/index.md`:
- New pages listed with wikilink + one-line description, under correct category

Append to `wiki-kb/wiki/log.md`:
- Entry format: `## [YYYY-MM-DD] ingest | Source Title`
- List all pages created or modified

Result: index and log current.

---

## Query

### Q1. Locate relevant pages — BLOCKING

Read `wiki-kb/wiki/index.md` to find candidate pages matching the query topic. Then read the top 3-5 most relevant pages.

Result: relevant wiki pages loaded.

### Q2. Synthesize answer — BLOCKING

Compose an answer from wiki content with `[[wikilinks]]` citations to source and concept pages. Format per user request (markdown page, table, slides, chart).

Result: answer with citations.

### Q3. Offer to file answer — CONFIRM

Ask user: "File this answer back into the wiki?" If yes, write it as a new page in the appropriate wiki directory (usually `wiki/analyses/` or `wiki/concepts/`), then update index and log.

Result: answer optionally saved to wiki.

---

## Lint

### L1. Scan for issues — BLOCKING

Read all wiki pages and check for:
- **Contradictions**: two pages making incompatible claims
- **Stale claims**: assertions superseded by newer sources
- **Orphans**: pages with no inbound links from other wiki pages
- **Missing pages**: important concepts/entities mentioned but lacking a dedicated page
- **Broken links**: `[[wikilinks]]` pointing to non-existent pages

Result: categorized issues list.

### L2. Report findings — CONFIRM

Present issues grouped by severity. For each: the problem, the pages involved, and a suggested fix.

Result: user reviews findings.

### L3. Apply fixes — BLOCKING

Fix each issue the user approves:
- Resolve contradictions by noting which source is newer / more authoritative
- Update stale pages with cross-reference to newer source
- Add cross-links to orphan pages from relevant entity/concept pages
- Create stub pages for important missing concepts
- Fix broken wikilinks

Result: issues resolved.

### L4. Log the lint pass — BLOCKING

Append to `wiki-kb/wiki/log.md`:
- `## [YYYY-MM-DD] lint | <N> issues found, <M> fixed`

Result: lint pass documented.

---

## Outputs

- Source summary pages in `wiki-kb/wiki/sources/` with frontmatter + wikilinks
- Entity pages in `wiki-kb/wiki/entities/` with backlinks to sources
- Concept pages in `wiki-kb/wiki/concepts/` with multi-source synthesis
- Analysis pages in `wiki-kb/wiki/analyses/` for cross-cutting synthesis
- Updated `wiki-kb/wiki/index.md` (content catalog by category)
- Updated `wiki-kb/wiki/log.md` (chronological event log)
- All pages use Obsidian-compatible `[[wikilinks]]` for graph navigation

## Error handling / Fallback

- **No source file found**: List contents of raw/ and ask user which file they mean. If raw/ is empty, suggest clipping an article first.
- **Source is too large**: Read in chunks. Summarize each chunk, then synthesize at the end.
- **Source contains images**: Read the markdown text first, then view referenced images in `wiki-kb/raw/assets/` for additional context.
- **Wikilink target doesn't exist**: Create a stub page for the missing entity/concept so the graph stays connected.
- **User disagrees with extraction**: Re-read the source with user's guidance. Flag the specific sections user wants emphasized.
- **index.md grows too large**: Suggest creating category-level sub-indexes (e.g., `wiki/concepts/_index.md`).

## Resources

- `references/llm-wiki-primer.md` — Karpathy's LLM Wiki pattern: core ideas, architecture, and design rationale
- `assets/templates/source-page.md` — Template for source summary pages in wiki/sources/
- `assets/templates/concept-page.md` — Template for concept pages in wiki/concepts/
- `assets/templates/entity-page.md` — Template for entity pages in wiki/entities/
- `evals/evals.json` — Trigger detection and core-function evaluations
