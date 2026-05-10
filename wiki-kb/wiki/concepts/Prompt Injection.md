---
title: "Prompt Injection"
tags:
  - concept
  - security
  - agent
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# Prompt Injection

## Definition

一种针对 LLM Agent 的安全攻击方式：通过精心设计输入，诱导模型忽略原有指令，执行攻击者意图的代码或泄露敏感信息。在 Agent 时代，其危害从"让模型说错话"升级为"让模型替你执行危险代码"。

## Key points

- Agent 真的有权限做事（读写文件、执行命令、调用 API），Prompt Injection 的攻击面远大于聊天机器人
- Anthropic 旧架构中的风险：Claude 生成的代码和 OAuth token/API key 在同一容器中，一次成功的注入可直接泄露凭证
- 防御方向：从 deny-list（禁止做什么）转向 capability-based（只允许做什么），最终目标是让凭证在物理上不可从执行环境触及
- 安全命题的认知翻转：传统安全假设"系统可信，防外部攻击"；Agent 架构里"系统生成的代码就是最大的不可信来源"

## Referenced in

- [[把 Agent 关进盒子里]] — 安全驱动沙盒化的核心论证

## Related concepts

- [[Agent 沙盒化]]
- [[Harness-Sandbox 分离]]
- [[Capability-based Security]]
