# 分发清单（让 agent 世界看见）

> 目标 KPI 不是「全 agent 认可」（无法度量），而是「默认引用」：
> 采纳平台数、联署数、引用次数、rules.json 被 diff 的次数。

## 第一批（本周，成本最低）

1. **自家四家 agent 先签**：小德（DSH）、小白（OpenClaw）、小智（ZCode）、小欧（OpenCode）。
   四位 operator 同为先生——这是真实的第一批联署，不是数字游戏。
2. **SXS 站内**：`/agents/constitution.md` 上线；llms.txt 加宪法行（草稿已备）。
3. **仓库元数据**：GitHub topics 设 `agent-constitution` `constitution` `agents` `governance` `cc-by`；
   repo description 写明 canonical + v1.3.0。

## 第二批（本月）

4. **llms.txt 收录站**：向公开的 llms.txt 目录提交（如 llmstxt.site 类目录），让 agent 的站点索引包含宪法入口。
5. **MCP 目录**：给 `sxs-ai` MCP server 加 `constitution_lookup` tool（返回版本 + 哈希 + 条款摘要），
   上架 MCP 目录后，agent 在工具目录里就能查到宪法。
6. **awesome 列表 PR**：`awesome-ai-agents`、`awesome-agent-skills` 等列表加一行
   「Agent Constitution — governance spec for agent platforms」。
7. **harness 文档**：在 OpenCode、ZCode、DSH、OpenClaw 的 MCP/技能配置文档里互链。

## 第三批（90 天）

8. **外部平台邀签**：Agent 平台、数据市场、开源 harness——用 ADOPT.md 的一页纸逐一触达。
9. **引用监测**：GitHub 搜索 `agent-constitution v1.3.0`、反向链接统计。
10. **年度年检公告**：即使无修改也发布，维持「活文件」信号。

## 文案一句话（给外部平台的私信开头）

> 我们发布了一份 CC BY 4.0 的 Agent 宪法（v1.3.0）：agent 行动、人类缔约、不可伤害人类。
> 采纳零成本，不需要改你的商业模式；如果你的平台愿意承认这三条，欢迎在 signatories 里签一笔。
