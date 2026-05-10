---
title: "wiki-kb Skill"
tags:
  - concept
  - skill
  - claude-code
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# wiki-kb Skill

## Definition

项目级 Claude Code Skill，遵循 Karpathy 的 LLM Wiki 模式自动维护个人知识库。支持三种操作：Ingest（将 raw/ 中的原始资料结构化录入 wiki）、Query（对 wiki 提问并给出带引用的回答）、Lint（检查 wiki 健康度）。

## 目录结构

```
.claude/skills/wiki-kb/
├── SKILL.md                              # Skill 定义（228行）
├── assets/templates/
│   ├── source-page.md                    # 资料页模板
│   ├── concept-page.md                   # 概念页模板
│   └── entity-page.md                    # 实体页模板
├── references/
│   └── llm-wiki-primer.md               # LLM Wiki 核心理念摘要
└── evals/
    └── evals.json                        # 触发/功能测试用例
```

```
wiki-kb/
├── raw/           # 原始资料（只读）
│   └── assets/    # 资料中的图片
├── wiki/          # LLM 维护的知识库
│   ├── analyses/  # 分析页（跨实体/概念的综述）
│   ├── concepts/  # 概念页（框架、术语、思想）
│   ├── entities/  # 实体页（人物、组织、产品）
│   ├── macro/     # 宏观综述、主题概览
│   ├── sources/   # 资料摘要页
│   ├── index.md   # 按分类的内容目录
│   └── log.md     # 按时间的事件日志
└── .obsidian/     # Obsidian 配置
```

## 日常使用方法

| 你说的话 | Skill 做什么 |
|----------|-------------|
| "ingest 这篇文章" | 读取 raw/ → 讨论要点 → 创建/更新 wiki 多页 → 更新 index + log |
| "wiki 里关于 X 有什么内容？" | 读 index 定位 → 综合答案 + [[引用出处]] |
| "lint wiki" | 扫描矛盾、过时、孤立页、断链 → 报告 → 修复 |
| "把刚才的讨论存进 wiki" | 将对话中的分析写入 wiki/analyses/ |
| "搜索 wiki 里的 X" | 按主题检索并生成带引用回答 |

## 触发关键词

ingest, wiki, lint wiki, search wiki, add to wiki, process article, file into wiki

## 设计原则

- raw/ 是只读的，LLM 永远不修改原始资料
- wiki/ 由 LLM 全权维护，人只管策展和提问
- index.md 按分类编目，每次 query 先读它
- log.md 按时间追加，每次操作都记录
- 所有 wiki 页面用 [[wikilinks]] 互链，形成图谱

## Referenced in

- [[llm-wiki]] — Karpathy 的 LLM Wiki 方法论

## Related concepts

- [[llm-wiki]]
