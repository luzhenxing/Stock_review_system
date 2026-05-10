---
title: "LLM Wiki"
tags:
  - concept
  - methodology
  - knowledge-base
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# LLM Wiki

## Definition

Andrej Karpathy 提出的个人知识库构建模式。核心理念：不让 LLM 在每次查询时从原始文档拼凑信息（RAG），而是让 LLM 增量式地构建和维护一个持久化的、互相链接的 Markdown wiki。wiki 是持久化、不断积累的人工制品——LLM 负责所有写作和维护，人只负责策展和提问。

## Key points

- **三层架构**：Raw sources（不可变原始资料）→ Wiki（LLM 维护的知识库）→ Schema（CLAUDE.md 定义结构和约定）
- **三种操作**：Ingest（摄入资料并更新多页 wiki）、Query（搜索 wiki 并给出带引用回答）、Lint（检查矛盾、过时、孤立页）
- **两个关键文件**：index.md（按分类的内容目录）、log.md（按时间的事件日志）
- **核心洞察**：人类放弃 wiki 是因为维护成本增长快于价值；LLM 不觉得无聊、不会忘记交叉引用、一次可更新 15 个文件
- 灵感来自 Vannevar Bush 的 Memex（1945）：一个私人的、精心策展的知识库，文档间的连接和文档本身一样有价值

## Referenced in

- [[wiki-kb-skill]] — 基于此模式实现的 Claude Code Skill

## Related concepts

- [[个性化 Agent 上下文]]
- [[wiki-kb-skill]]
