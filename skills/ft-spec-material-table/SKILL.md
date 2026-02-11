---
name: ft-spec-material-table
description: Build clean product specification and material information tables for foreign-trade listings. Use when seller notes are incomplete and a structured spec table is needed for Amazon, Taobao, 1688, or independent storefront product pages.
---

# ft-spec-material-table

Convert scattered product data into a buyer-friendly spec table.

## Workflow

1. Normalize source input (chat notes, factory sheet, image text, PDF snippets).
2. Map fields into a standard schema.
3. Mark each field as one of: Provided / Estimated / Missing.
4. Generate two table layers:
   - Buyer-facing concise table
   - Internal QC table with verification status
5. Add a "supplier confirmation checklist" for missing high-risk fields.

## Standard Spec Schema

- Product Name
- Model / SKU
- Category
- Main Material
- Secondary Material
- Size (L x W x H)
- Weight (net / gross)
- Color Options
- Surface / Finish
- Craft / Process
- Package Includes
- Carton Size
- MOQ
- Lead Time
- Certifications (if any)
- Country of Origin
- Care / Maintenance

## Output Template

```md
## Buyer Spec Table
| Field | Value |
|---|---|

## Material Composition Table
| Part | Material | Ratio / Thickness | Notes |
|---|---|---|---|

## Internal QC Table
| Field | Status (Provided/Estimated/Missing) | Source | Risk |
|---|---|---|---|

## Supplier Confirmation Questions
1.
2.
3.
```

## Quality Bar

- Use SI units by default, add imperial in parentheses for US channels.
- Do not fabricate certifications.
- Highlight fields that affect return/dispute risk (size tolerance, coating, fragile parts).

---

## 中文版本

将分散参数整理为可读、可核验的规格/材质表。

### 工作流

1. 统一输入来源（聊天记录、工厂表、图片文字、PDF）。
2. 按标准字段映射产品信息。
3. 标记字段状态：已提供 / 估算 / 缺失。
4. 输出两层表格：
   - 面向买家的精简参数表
   - 面向内部的 QC 校验表（含来源与风险）
5. 追加供应商确认清单，优先补齐高风险参数。

### 质量标准

- 默认公制单位，面向美国渠道加英制括号。
- 不得虚构认证信息。
- 必须突出容易引发退换货争议的字段（公差、涂层、脆弱部件等）。
