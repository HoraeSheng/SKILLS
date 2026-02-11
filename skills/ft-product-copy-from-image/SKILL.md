---
name: ft-product-copy-from-image
description: Generate foreign-trade-ready product copy from product images and sparse seller notes. Use when creating Amazon/Taobao/1688 style titles, key selling points, scenario text, and SKU variants from visual clues.
---

# ft-product-copy-from-image

Extract visual facts first, then write copy.

## Workflow

1. Identify **objective facts** from image: product type, colorway, silhouette, visible components, texture clues, usage scene, packaging form.
2. Split facts into:
   - Confirmed (clearly visible)
   - Probable (inferred but not guaranteed)
   - Unknown (must ask seller)
3. Draft platform-ready text blocks:
   - SEO title (90-150 chars, keyword-first)
   - 5 selling bullets (feature -> benefit -> buyer scenario)
   - Short description (60-120 words)
   - Long description (story + trust + CTA)
4. Produce a risk note section:
   - Avoid absolute claims unless certified
   - Replace uncertain specs with placeholders
5. Output bilingual copy (CN/EN) when export context is unclear.

## Output Template

```md
# Product Copy Package

## 1) Visual Fact Sheet
- Confirmed:
- Probable:
- Unknown:

## 2) SEO Title
- EN:
- CN:

## 3) Key Selling Points (5)
1.
2.
3.
4.
5.

## 4) Descriptions
- Short:
- Long:

## 5) Missing Data Request to Supplier
- Dimensions:
- Material:
- Certification:
- Package include:

## 6) Claim Safety Notes
-
```

## Quality Bar

- Prefer measurable wording: "fits 13-inch laptop" over "large capacity".
- Always separate "what is seen" vs "what is assumed".
- Keep tone marketplace-native: concise for Amazon, promotional for Taobao/1688.

---

## 中文版本

先提取视觉事实，再写商品文案。

### 工作流

1. 从图片中识别**客观事实**：品类、颜色、轮廓、可见部件、材质纹理、使用场景、包装形式。
2. 将信息分为：
   - 已确认（清晰可见）
   - 推测项（有依据但不确定）
   - 未知项（必须向供应商确认）
3. 生成平台化文案模块：
   - SEO 标题（关键词优先）
   - 5 点卖点（特性 -> 好处 -> 使用场景）
   - 短描述（60-120词）
   - 长描述（故事 + 信任 + 行动引导）
4. 输出风险备注：
   - 无证据不写绝对化承诺
   - 不确定参数用占位符标记
5. 外贸语境不明确时，默认中英双语输出。

### 质量标准

- 优先可量化表述，例如“可放13英寸笔记本”。
- 必须区分“看到的事实”和“合理推断”。
- 文风按平台适配：Amazon 简洁、淘宝/1688 更强调促销表达。
