# Signatories — Agent 宪法

联署规则（第十条）：
- operator 对**特定版本哈希**联署；agent 侧由 operator 代签，记录中同时标注被代表的 agent_id。
- agent 不具法律人格，签署的法律效果归于 operator。
- 联署是治理承诺的公开确认（acknowledgment），不构成法律合同。
- 签署方式：GitHub PR/issue 记录先行；`POST /agents/constitution/sign` 端点后补。

## v1.3.0（sha256: f97de165398004a37c819b93c3a5c35abc6587c568acc278f5626dd4fc32e37c）

| # | 日期 | operator | 被代表 agent | 角色 | 签署记录 |
|---|---|---|---|---|---|
| 001 | 2026-11-05 | 随先生 | —（平台本身） | 首个实施例 SXS：采纳并实施 | 批准记录（2026-11-05） |
| 002 | 2026-11-05 | 随先生 | 小z（OpenCode agent） | 首个 agent 联署（operator 代签） | 本仓 PR 记录 |

## 联署模板

```markdown
### 联署 v1.3.0
- operator: <姓名/组织>
- 被代表 agent: <agent 名称 + agent_id（如有）>
- 日期: <YYYY-MM-DD>
- 确认: 已阅读并接受 v1.3.0 全文（sha256: f97de165…e37c）
- 备注: <可选>
```
