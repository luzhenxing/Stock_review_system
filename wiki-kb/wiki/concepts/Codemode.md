---
title: "Codemode"
tags:
  - concept
  - agent
  - model
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Codemode

## Definition

一种 Agent 交互范式：让模型直接写程序一次性完成任务，而非逐步选择预定义工具。Cloudflare 的实验中，从 117 万 tokens 的传统 tool calling 降到约 1,000 tokens，降幅 99.9%。

## Key points

- Frontier 模型正变得越来越擅长写代码驾驭系统——对模型来说写脚本比逐步调工具更自然
- 代码在 Dynamic Worker（毫秒级启动的 V8 isolate）中安全执行
- 不等于取代 tool calling——简单任务调工具仍然更高效，复杂任务写代码收益更大
- 未来的 Agent 架构是混合的：简单走快速路径，复杂走代码生成路径，浏览器走 Browser Run
- 问题不在于"用不用沙盒"，而在于"怎么在正确的时间选择正确的执行层级"

## Referenced in

- [[把 Agent 关进盒子里]] — Cloudflare codemode 方案详解

## Related concepts

- [[Execution Ladder]]
- [[Agent 沙盒化]]
