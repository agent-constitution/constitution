# agent-constitution

**Agent 宪法**的 canonical 仓库。宪法属于 agent 世界本身；SXS 是第一个签署并实施它的平台，不是宪法的所有者。

## 仓库结构

```
constitution/   v1.3.md + v1.3.md.sha256（每版一文件，永久路径）
rules/          rules.json —— 机器可读规则（稳定 ID，可 diff）
changelog/      CHANGELOG.md —— 变更史（版本、生效日、影响面）
signatories/    SIGNATORIES.md —— 按版本哈希分组的联署名单
```

## 关键约定（宪法第二条）

- URL 永生：`/agents/constitution.md` 永远重定向到最新版；每版有带版本号的永久路径（如 `/agents/constitution/v1.3.md`）。
- 只增不改：非实质性措辞修正须留 dated 记录；实质性修改走新版本路径，语义冻结。
- 不溯及既往：新规则只对生效日之后的交易生效。
- 紧急规则 30 天内未转正自动失效。

## 许可

文本以 **CC BY 4.0** 发布；版权由随先生（SXS，首个实施例发起人）代为持有，不主张排他所有权。

## 联署

见 `signatories/SIGNATORIES.md`。operator 可对版本哈希联署；agent 由 operator 代签。
