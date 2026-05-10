---
title: "把 Agent 关进盒子里"
source: "https://mp.weixin.qq.com/s/7etnm7OzErsvFK7dSQ3eog"
author:
  - "[[中国人本来就聪明]]"
published: 2026-04-16
ingested: 2026-05-10
tags:
  - source
  - agent
  - security
  - sandbox
  - infra
---

# 把 Agent 关进盒子里

## Summary

2026 年 4 月中旬，Cloudflare、Anthropic、OpenAI 集中发布了 Agent 沙盒化方案，标志着 AI Agent 的执行环境正在全面升级。沙盒化远不止"加个隔离环境"——它从安全模型（Prompt Injection 成为架构假设）、成本结构（Durable Objects hibernation 让空闲成本趋零）、开发范式（Harness-Sandbox-Session 三层解耦）三个维度重构了 Agent 基础设施。文章详细拆解了 Execution Ladder、Codemode、Manifest 抽象、三种沙盒哲学分野，以及沙盒化的隐形成本和未来 12 个月的四个判断。

## Key takeaways

- 安全命题的认知翻转：重点从"防外部攻击"转移到"防 Agent 自己害自己"——Agent 生成的代码就是最大的不可信来源
- Harness（大脑）和 Sandbox（双手）必须物理分离，凭证在物理上不可从执行环境触及
- Agent 的"一对一"特性颠覆了传统容器经济学：从"提高单机利用率"变成"降低空闲持有成本"
- Cloudflare Execution Ladder：沙盒不是非黑即白，从 Workspace 到完整 OS Sandbox 分 5 级，每级增量释放能力
- 模型正从 tool calling 转向写代码驾驭系统——token 消耗可降低 99.9%
- Session ≠ Context Window：Session 是 Agent 的版本控制、调试器和审计日志
- 三种沙盒哲学：Anthropic 自上而下、Cloudflare 自下而上、OpenAI 中间切入，终点一致
- 沙盒层已成为 Agent 平台的核心竞争力，类似云计算时代的操作系统和容器编排

## Entities

- [[Cloudflare]]
- [[Anthropic]]
- [[OpenAI]]
- [[Vercel]]
- [[E2B]]
- [[Daytona]]
- [[Runloop]]
- [[Blaxel]]
- [[中国人本来就聪明]]

## Concepts

- [[Agent 沙盒化]]
- [[Prompt Injection]]
- [[Harness-Sandbox 分离]]
- [[Execution Ladder]]
- [[Codemode]]
- [[Session 持久化]]
- [[Capability-based Security]]

## Notable quotes

> 传统安全模型默认假设"系统本身可信，需要防御的是外部攻击者"。但在 Agent 架构里，系统自己生成的代码就是最大的不可信来源。

> 沙盒化就是一次架构升级，任何架构升级都需要付出学习和重构的成本。

> 谁控制了 Agent 的执行环境，谁就在很大程度上控制了 Agent 的可靠性、安全性和成本结构。
