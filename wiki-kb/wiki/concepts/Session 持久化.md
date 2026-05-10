---
title: "Session 持久化"
tags:
  - concept
  - agent
  - infra
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Session 持久化

## Definition

Session 不等于 Context Window——上下文窗口只是当前喂给模型的内容，Session 记录从开始到现在的全部历史事件。Session 同时扮演 Agent 的版本控制系统、调试器和审计日志。

## Key points

- Session 是追加式不可变事件日志，记录每次模型响应、每次工具调用、每次状态变化
- 支持按位置切片读取、回退查看前因、失败重试时重读完整上下文
- Cloudflare 的 Session API 支持 forking（分支对话）和非破坏性压缩、基于 SQLite FTS5 的全文搜索
- 持久化对 Agent 比对传统应用更重要——Agent 执行是非确定性的，不可变事件流是唯一可靠的调试手段
- Harness 崩溃后可以通过 `wake(sessionId)` 从最后一条事件继续执行
- 沙盒快照 + Session 持久化共同支撑长程 Agent 运行

## Referenced in

- [[把 Agent 关进盒子里]] — Session 持久化作为沙盒化的核心支撑

## Related concepts

- [[Harness-Sandbox 分离]]
- [[Agent 沙盒化]]
- [[长程 Agent]]
