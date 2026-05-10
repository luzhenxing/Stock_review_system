---
title: "Harness-Sandbox 分离"
tags:
  - concept
  - agent
  - architecture
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Harness-Sandbox 分离

## Definition

Agent 架构的核心解耦模式。Harness（大脑）负责调用模型和路由工具请求，Sandbox（双手）负责代码执行和文件编辑，两者物理分离。灵感来自操作系统虚拟化硬件的思路。

## Key points

- **三个组件**：Session（追加式事件日志）、Harness（调用 Claude 并路由工具请求）、Sandbox（代码执行和文件编辑）
- **核心设计**：Harness 不直接执行代码，Sandbox 永远接触不到凭证
- **接口标准化**：`execute(name, input) → string`，Sandbox 可以任意替换（容器、手机、甚至 Pokémon 模拟器）
- **失败恢复**：Sandbox 死了不影响任务——Harness 把错误返回模型，模型决定是否重试；Harness 崩溃也不影响——Session 独立存储，新 Harness 通过 `wake(sessionId)` 恢复
- **性能收益**：Anthropic 解耦后 p50 TTFT 下降约 60%，p95 TTFT 下降超过 90%
- **哲学含义**：Sandbox 从"宠物"变成了"牲畜"——可随意替换、横向扩展、按需分配

## Referenced in

- [[把 Agent 关进盒子里]] — Anthropic Managed Agents 架构详解

## Related concepts

- [[Agent 沙盒化]]
- [[Session 持久化]]
- [[Prompt Injection]]
