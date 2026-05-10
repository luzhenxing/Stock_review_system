---
title: "Agent 配置 Git 管理"
tags:
  - concept
  - git
  - agent
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Agent 配置 Git 管理

## Definition

将 `~/.claude/` 目录作为 git 仓库管理，用版本控制追踪所有 Skill、Rules、CLAUDE.md 的变更，实现跨设备同步。

## Key points

- `.gitignore` 使用白名单模式：先用 `*` 忽略一切，再用 `!` 显式放行 CLAUDE.md、skills/、rules/、agents/
- 运行时文件（对话历史、OAuth 凭据、缓存）不会被意外提交
- 支持在不同分支上实验新的 Skill 配置
- 新机器上装完 Claude Code，git clone 拉完配置，Agent 立刻"认识你"——全程不到五分钟
- Agent 不再绑定在某一台机器上，它跟着 git 仓库走

## Referenced in

- [[Agent 的超级进化]] — Git 管理方案的详细描述

## Related concepts

- [[个性化 Agent 上下文]]
- [[Skill 可组合性]]
