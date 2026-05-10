---
title: "/eat 知识吸收"
tags:
  - concept
  - skill
  - agent
created: 2026-05-10
updated: 2026-05-10
source_count: 1
---

# /eat 知识吸收

## Definition

一个主动吸收外部知识的 Skill，灵感来自《千与千寻》的无脸男。给它 GitHub 仓库、文章 URL、代码片段、技术文档、甚至别人的 Skill 目录，它会深度分析后建议最合适的消化形式——新建 Skill、更新规则、还是扩展已有 Skill。

## Key points

- **五步工作流**：输入识别与获取→深度分析→影响扫描（检查现有 Skills/CLAUDE.md/rules）→消化建议→执行消化
- **过滤机制**（吃之前判断）：
  - 一次性知识不吸收（如某个 API 的参数）
  - 一行规则能搞定的不新建 Skill
  - Claude 已知的通用知识不吸收
  - 已有 Skill 覆盖 80% 的扩展已有的
- **常用场景**：消化别人分享的工作流、技术文档更新、竞品分析、论文和开源项目
- 消化的目标是留下精华，不是堆积数量——无脸男吃太多也会失控

## Referenced in

- [[Agent 的超级进化]] — /eat 的完整设计

## Related concepts

- [[Skill 可组合性]]
- [[Agent 自进化]]
- [[Agent 配置 Git 管理]]
