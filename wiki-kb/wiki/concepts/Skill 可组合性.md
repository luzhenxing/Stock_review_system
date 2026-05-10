---
title: "Skill 可组合性"
tags:
  - concept
  - skill
  - agent
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Skill 可组合性

## Definition

Skill 是 Claude Code 中可复用的能力模块，每个 Skill 一个目录、核心是一份 SKILL.md。Skill 和传统"模板"的本质区别在于可组合性——Agent 可以在一次任务中自动识别并协调使用多个 Skill，形成流水线。模板是孤立的固定流程，Skill 是可自由组合的能力积木。

## Key points

- 每个 Skill 只做一件事，但组合起来就能解决完整的业务问题
- Agent 自动判断该调用哪些 Skill、按什么顺序调用——不需要你手动编排
- 渐进式披露（Progressive Disclosure）：L1 始终在上下文（~100 tokens），L2 触发时加载，L3 按需读取。几十个 Skill 对上下文窗口压力很小
- Skill 通过系统级 prompt 注入，权重高于模型默认行为——你在 Skill 里定义的流程能覆盖模型默认行为
- 对新手友好的是模板，对深度用户上限高的是 Skill

## Referenced in

- [[Agent 的超级进化]] — Skill 体系的详细讨论

## Related concepts

- [[个性化 Agent 上下文]]
- [[Agent 自进化]]
- [[-eat 知识吸收]]
