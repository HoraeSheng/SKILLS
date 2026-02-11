---
name: ft-marketplace-listing-localization
description: Localize one product listing into multiple marketplace styles (Amazon, Taobao, 1688) while keeping product facts consistent. Use when adapting title, bullets, detail narrative, and CTA tone by audience and channel.
---

# ft-marketplace-listing-localization

Keep facts fixed, change communication style by channel.

## Workflow

1. Freeze a single source-of-truth fact sheet.
2. Use `references/channel-style-guide.md` to map each section:
   - Title logic
   - Bullet/卖点 structure
   - Detail narrative depth
   - CTA style
3. Generate channel variants from the same facts.
4. Run consistency check to ensure no cross-channel contradiction.

## Output Template

```md
## Shared Fact Sheet
-

## Amazon Version
- Title:
- Bullets:
- Description:

## Taobao Version
- 主标题:
- 核心卖点:
- 详情文案:

## 1688 Version
- 工厂供货标题:
- 批发卖点:
- 交易条款文案(MOQ/交期/打样):

## Consistency Diff Check
- No-conflict fields:
- Needs review:
```

---

## 中文版本

保持商品事实一致，按平台改写表达风格。

### 工作流

1. 先冻结统一事实底稿（参数、卖点、交易条件）。
2. 结合 `references/channel-style-guide.md` 做结构化改写：
   - 标题逻辑
   - 卖点表达
   - 详情深度
   - CTA 语气
3. 基于同一事实生成 Amazon / 淘宝 / 1688 三端版本。
4. 执行一致性核对，排除跨平台冲突。

### 质量标准

- 允许“表达差异”，不允许“事实差异”。
- 1688 文案优先补充 MOQ、交期、打样与定制能力。
