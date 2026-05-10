---
title: "Capability-based Security"
tags:
  - concept
  - security
  - agent
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Capability-based Security

## Definition

一种安全模型：从 deny-list（禁止做什么）转向 capability-based（只允许做什么），再进一步——让凭证在物理上不可从执行环境触及。Agent 执行环境默认几乎没有任何权限，需要显式授予每种能力。

## Key points

- 传统 deny-list 模型在 Agent 场景中失效——你无法穷举模型可能做出的所有危险行为
- Capability-based：Execution Ladder 中每一层默认无权限，增量授予
- 凭证注入最终形态：不在环境变量中、不在容器启动时进入，而是通过网络层 egress proxy 动态注入
- Anthropic 和 Cloudflare 在此思路上高度对齐
- Cloudflare Dynamic Worker 的默认状态就是 `globalOutbound: null`（无网络访问）

## Referenced in

- [[把 Agent 关进盒子里]] — 新旧安全模型的对比

## Related concepts

- [[Agent 沙盒化]]
- [[Prompt Injection]]
- [[Execution Ladder]]
