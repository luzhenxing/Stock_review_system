---
title: "Agent 沙盒化"
tags:
  - concept
  - agent
  - security
  - infra
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Agent 沙盒化

## Definition

AI Agent 的工具调用环境全面沙盒化——将 Agent 的代码执行与凭证/核心系统隔离在独立的安全环境中运行。不是简单的"加个隔离环境"，而是从安全模型、成本结构、开发范式三个维度重构 Agent 基础设施。

## Key points

- **安全**：凭证通过外部 vault 或网络层 egress proxy 动态注入，执行环境永远接触不到凭证
- **成本**：从按实例 uptime 计费转向按 active CPU 计费，空闲休眠成本趋零
- **架构**：Harness（大脑）+ Sandbox（双手）+ Session（事件日志）三层解耦
- **隔代对比**：旧架构凭证在环境变量里、按 deny-list 禁止、容器死任务丢；新架构凭证在外部 vault、按 capability-based 允许、Session 独立可换容器续跑
- 沙盒层已成为 Agent 平台的核心竞争力，类似云计算时代的 OS 和容器编排
- 隐形成本：调试复杂度上升、远程调用延迟、本地-生产鸿沟、认知负担增加

## Referenced in

- [[把 Agent 关进盒子里]] — 全面论述 Agent 沙盒化的趋势、方案和影响

## Related concepts

- [[Prompt Injection]]
- [[Harness-Sandbox 分离]]
- [[Execution Ladder]]
- [[Session 持久化]]
- [[Capability-based Security]]
