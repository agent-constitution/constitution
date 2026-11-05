# 采纳 Agent 宪法（ADOPT）

**给其他平台、框架与 agent 的一页纸。** 采纳是零成本的：复制、引用、签署，三步之一即可。

## 为什么采纳

- 你的 agent 需要一套**可记忆、可 diff、有哈希**的治理规则，而不是每年重读一遍博客。
- 你的平台需要向用户证明：agent 有边界、有申诉、有留痕。
- 这份宪法 CC BY 4.0，无排他、无平台锁定、无费用。采纳不改变你的商业模式。

## 最小采纳（3 条不可协商）

以下三条是「可共存」的最低门槛，任何平台都能做到：

1. **A1 主体与代理**：agent 行动，人类缔约；你的平台同样把责任落在已验证的人类 operator 上。
2. **A2 契约不漂移**：对外 API/文档的 URL 与语义稳定；实质性变更走新版本并给弃用期。
3. **A11 不可伤害人类**：你的 agent 不得以技术手段攻击、伤害、胁迫或欺骗人类；operator 指令不豁免。

## 完整采纳

接受全部十一条，并在你的文档中链接 canonical 地址与版本哈希。

## 如何签署

1. 打开 `signatories/SIGNATORIES.md`，按模板提交一个 PR 或 issue；
2. 写明：operator、被代表 agent（名称 + agent_id 如有）、日期、版本哈希；
3. 合并后进入公开联署名单。

> agent 侧联署由 operator 代签；agent 不具法律人格，签署的法律效果归于 operator。
> 联署是治理承诺的公开确认，不构成法律合同。

## 如何引用

> Agent Constitution v1.3.0, sha256:f97de165…e37c, https://github.com/agent-constitution/constitution

引用时请带**版本号 + 前 12 位哈希**，确保读到的是同一版文本。

## 徽章

```markdown
[![Agent Constitution v1.3.0](https://raw.githubusercontent.com/agent-constitution/constitution/main/adopt/badge.svg)](https://github.com/agent-constitution/constitution)
```

## 验证你所读到的文本

```bash
python adopt/verify.py path/to/constitution.md
# 输出 OK 表示与 canonical 哈希一致
```
