# Wiki Index

## Sources

- [[股票大作手回忆录]] — 杰西·利弗莫尔四起四落的交易生涯：趋势、最小阻力、心理纪律的永恒智慧
- [[Agent 的超级进化]] — 个人超级 Agent = 通用 Agent + 个性化上下文，从 Skill 体系、自进化到长程运行的完整方法论
- [[把 Agent 关进盒子里]] — Agent 沙盒化：安全、成本、架构三重维度的基础设施重构
- [[个人业务Agent升级指南]] — 用 Agent 改造投研和内容生产，$500/月替代 5 人团队，从三层架构到 AaaS 商业模式

## Concepts

### Trading

- [[市场最小阻力路线]] — 价格沿阻力最小的方向运动，交易者的任务是等市场自己界定这条路线
- [[趋势与耐心坚守]] — 大钱不在个别波动而在主要趋势；正确判断不难，耐心坚守才是关键
- [[投机者的人性弱点]] — 亏损时希望是最后一天，盈利时害怕利润飞走——必须和天性反着做
- [[金字塔建仓法]] — 试探建仓→有利润才加码→开头便错立刻止损
- [[利弗莫尔交易规则]] — 15 条真金白银换来的铁律：顺势、止损、做领头羊、不摊平亏损

### AI Agent

- [[Agent 沙盒化]] — Agent 执行环境全面沙盒化：安全、成本、开发范式三重重构
- [[Prompt Injection]] — LLM Agent 安全攻击：从"让模型说错话"到"让模型执行危险代码"
- [[Harness-Sandbox 分离]] — Agent 架构核心解耦模式：大脑与双手物理分离
- [[Execution Ladder]] — Cloudflare 分层沙盒模型：从 Workspace 到完整 OS 的五级渐进谱系
- [[Codemode]] — 让模型写代码替代逐步调工具，token 消耗降低 99.9%
- [[Session 持久化]] — Session ≠ Context Window，是 Agent 的版本控制 + 调试器 + 审计日志
- [[Capability-based Security]] — 从 deny-list 到 capability-based：默认无权限，显式授予
- [[个性化 Agent 上下文]] — 核心公式：个人超级 Agent = 通用 Agent + 个性化上下文
- [[Skill 可组合性]] — Skill 不是模板，是可自由组合的能力积木，支持渐进式披露加载
- [[Agent 自进化]] — 正负反馈闭环驱动的持续优化机制，每次反馈持久化到文件系统
- [[-eat 知识吸收]] — 主动吸收外部知识的机制，含过滤策略防止配置膨胀
- [[长程 Agent]] — Agent 的终极形态：接受大目标后自主运行数小时，关键节点才找人确认
- [[Agent 配置 Git 管理]] — ~/.claude/ 用 git 管理，白名单 .gitignore，跨设备同步
- [[渐进式披露]] — Skills 的 L1/L2/L3 三层加载策略，避免上下文窗口过载
- [[llm-wiki]] — Karpathy 的 LLM Wiki 模式：增量式构建持久化知识库
- [[wiki-kb-skill]] — Claude Code Skill：LLM Wiki 模式的自动化实现

### 业务 Agent 化

- [[算法杠杆]] — Agent 化是继时间、产品、平台之后的第四种商业杠杆
- [[Agent三层架构]] — 个人 Agent 系统的三层次：知识库（记忆）→ Skills（判断）→ CRON（执行）
- [[Skills显性化]] — 把隐性的判断标准写成结构化的 if-then 规则，让 AI 按你的框架工作
- [[AaaS (Agent as a Service)]] — Agent 即服务：卖结果不卖工具，替代传统 SaaS
- [[爆款内容框架]] — 系统化研究爆款规律→提炼可复用公式→喂给 AI 的内容生产方法论
- [[人机协作内容生产线]] — 选题 AI 主导、写作人机协作、发布全自动，效率提升 75%

### Skill 模板

- [[Skill模板-美股价值投资框架]] — 财报→四维评估→A/B/C/D 评级
- [[Skill模板-比特币抄底模型]] — 6 项指标交叉验证的分级抄底信号
- [[Skill模板-美股市场情绪监控]] — 机构/散户/估值/杠杆四维情绪监控，3 项预警→减仓
- [[Skill模板-宏观流动性监控]] — 净流动性公式 + SOFR + MOVE，提前 48h 预警市场暴跌

## Entities

### Trading

- [[杰西·利弗莫尔]] — 华尔街传奇交易员，四起四落，趋势交易的鼻祖
- [[埃德温·勒菲弗]] — 《股票大作手回忆录》作者，前华尔街经纪商
- [[丁圣元]] — 中文版译者，补充历史行情图和交易规则附录
- [[老帕特里奇]] — "这是牛市，你知道"——利弗莫尔的间接导师

### AI Agent

- [[Anthropic]] — Claude 模型开发公司，Harness-Sandbox 分离架构提出者
- [[Cloudflare]] — Agent 沙盒基础设施：Sandboxes、Project Think、Browser Run
- [[OpenAI]] — Agents SDK 原生沙盒执行，Manifest 抽象 + 7 家沙盒提供商生态
- [[Vercel]] — OpenAI Agents SDK 官方沙盒扩展（Firecracker microVM）
- [[E2B]] — 代码执行沙盒老玩家，按 vCPU-秒计费
- [[Daytona]] — 90ms 极致冷启动沙盒，Docker in Docker
- [[Runloop]] — 长时有状态 Agent 沙盒，Custom bare-metal hypervisor
- [[Blaxel]] — "sleeps but never dies" 沙盒，25ms resume
- [[Claude Code]] — Anthropic 的命令行 AI Agent 工具
- [[LangChain]] — LLM 应用开发框架
- [[HappyClaw]] — 将 Mac mini 改造成 24 小时在线 Agent 服务器的开源项目
- [[OpenClaw]] — 本地持久化 Agent 守护进程，支持多渠道接入
- [[中国人本来就聪明]] — 微信公众号作者，Agent 领域深度实践者

### 内容创作者

- [[XinGPT]] — X 博主（@xingpt），算法杠杆/AaaS 提出者，投研与内容 Agent 化实践者

## Analyses

- [[Agent能力两视角对比]] — 超级进化 vs 升级指南：一个教你怎么造 Agent，一个让你看造出来能做什么

## Macro

_待创建_
