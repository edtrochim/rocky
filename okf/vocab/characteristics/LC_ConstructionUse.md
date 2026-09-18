---
id: characteristic:LC_ConstructionUse
kind: vocab_characteristic
title: LC_ConstructionUse
lchs_type: LC_ConstructionUseType
lccs3_types:
- LC_ConstructionUse
properties:
- constructionUse
links:
- rel: allows
  id: enum:ConstructionUsesEnum
  path: ../enums/ConstructionUsesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_ConstructionUse

Construction Use Characteristic

LChS reference name `LC_ConstructionUse` (schema type `LC_ConstructionUseType`). LCCS3 `xsi:type`: `LC_ConstructionUse`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `constructionUse` | ConstructionUsesEnum | `Agricultural`, `Residential`, `Commercial`, `Industrial`, `Utlility` |  | Construction Use |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
