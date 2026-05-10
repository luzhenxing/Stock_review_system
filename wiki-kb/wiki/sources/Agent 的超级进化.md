---
title: "Agent 的超级进化"
source: "https://mp.weixin.qq.com/s/jWO7bxOK1N-weI0gtRpYWw"
author:
  - "[[中国人本来就聪明]]"
published: 2026-03-02
ingested: 2026-05-10
tags:
  - source
  - agent
  - skill
  - claude-code
---

# Agent 的超级进化

## Summary

文章系统阐述了个人 Agent 体系建设的方法论。核心理念：个人超级 Agent = 通用 Agent + 个性化上下文。作者通过半年高强度使用 Claude Code、积累数十个 Skill 的实践经验，提出了一套从上下文架构（CLAUDE.md + Rules + Skills）、自进化机制（正负反馈闭环）、外部知识吸收（/eat）、到 Git 管理与长程独立运行的完整体系。核心观点是：拉开 Agent 差距的不是模型能力或框架精巧度，而是你注入的个性化上下文——而这些上下文不会过时，具有复利效应。

## Key takeaways

- 个人超级 Agent = 通用 Agent + 个性化上下文，上下文完全由你定义
- 上下文分两层：CLAUDE.md + Rules 定义"怎么思考"，Skills 定义"能做什么"
- Skill 不是模板——它是可组合的能力积木，Agent 能自动识别并协调使用多个 Skill
- 自进化靠两个闭环：负反馈（纠错→写规则→下次避免）、正反馈（成功→提炼为 Skill）
- `/eat` 像无脸男一样吸收外部知识，但要经过过滤：一次性知识、通用知识、已有覆盖的不吸收
- `~/.claude/` 用 git 管理 + 白名单 .gitignore，实现跨设备同步
- 经验的沉淀路径：行为约束→rules/，能力流程→skills/，全局总纲→CLAUDE.md
- 终极形态：长程独立运行（Long Horizon Agents），Agent 从工具变成协作伙伴

## Entities

- [[Claude Code]]
- [[Anthropic]]
- [[HappyClaw]]
- [[OpenClaw]]
- [[LangChain]]
- [[中国人本来就聪明]]

## Concepts

- [[个性化 Agent 上下文]]
- [[Skill 可组合性]]
- [[Agent 自进化]]
- [[-eat 知识吸收]]
- [[长程 Agent]]
- [[Agent 配置 Git 管理]]
- [[渐进式披露]]

## Notable quotes

> 花在写 Agent 框架上的时间，不如花在整理业务上下文上。

> 你从施工者变成了总包——关注的不再是砖怎么砌，而是房子盖得对不对。

> Agent 越强，你的专业"主见"就越重要。你是那个定方向的人，Agent 是那个高效执行的人。搞反了，麻烦比没有 Agent 还大。

> 拉开差距的不再是谁知道得多，而是谁能把知识用出来。
