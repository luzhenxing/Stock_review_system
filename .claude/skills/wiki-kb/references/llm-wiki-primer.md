# LLM Wiki Pattern — Primer

From Andrej Karpathy's gist: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## Core idea

Instead of RAG (retrieve raw documents at query time), the LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files between you and the raw sources. Knowledge is compiled once and kept current, not re-derived on every query.

## Three layers

1. **Raw sources** — immutable source documents. LLM reads from them, never modifies.
2. **Wiki** — LLM-generated markdown files (summaries, entity pages, concept pages, synthesis). LLM owns this entirely.
3. **Schema** — a document (CLAUDE.md or AGENTS.md) telling the LLM wiki structure, conventions, and workflows.

## Three operations

- **Ingest**: read source → discuss with user → create/update wiki pages → update index + log
- **Query**: search wiki → synthesize answer with citations → optionally file back
- **Lint**: scan for contradictions, stale claims, orphans, missing pages → report → fix

## Two key files

- **index.md**: content catalog by category. LLM reads this first on every query.
- **log.md**: chronological, append-only. Format: `## [YYYY-MM-DD] operation | details`

## Design rationale

Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored, don't forget cross-references, and can touch 15 files in one pass. The human curates sources and asks questions; the LLM handles all bookkeeping.

Related to Vannevar Bush's Memex (1945): a personal, curated knowledge store with associative trails, where connections between documents are as valuable as the documents themselves.
