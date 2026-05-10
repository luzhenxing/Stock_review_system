---
title: "Execution Ladder"
tags:
  - concept
  - agent
  - infra
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Execution Ladder

## Definition

Cloudflare 提出的 Agent 执行环境分层模型。沙盒化超越了"有沙盒"和"没沙盒"的二元划分，是一个从受限到开放的连续谱系。核心原则：Agent 在最底层就应该有用，每一层都是增量能力。

## Key points

- **Tier 0 — Workspace**：持久化虚拟文件系统（SQLite + R2），最简单的 Agent 不需要容器就能工作
- **Tier 1 — Dynamic Worker**：沙盒化 JS，无网络访问，毫秒级启动
- **Tier 2 — Dynamic Worker + npm**：运行时包解析
- **Tier 3 — Browser Run**：无头浏览器自动化，支持 Puppeteer/Playwright/CDP/MCP
- **Tier 4 — Cloudflare Sandbox**：完整 OS 访问，git clone、npm test、cargo build，快照恢复仅需 2 秒
- 渐进式能力释放：既保证安全性（默认最小权限），又避免过度工程化

## Referenced in

- [[把 Agent 关进盒子里]] — Cloudflare 分层沙盒模型详解

## Related concepts

- [[Agent 沙盒化]]
- [[Capability-based Security]]
