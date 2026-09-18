---
id: characteristic:LC_WaterChemistryCharacteristic
kind: vocab_characteristic
title: LC_WaterChemistryCharacteristic
lchs_type: LC_WaterChemistryCharacteristicType
lccs3_types:
- LC_WaterChemistry
properties:
- nutrientLevel
links:
- rel: allows
  id: enum:NutrientLevelsEnum
  path: ../enums/NutrientLevelsEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_WaterChemistryCharacteristic

Water Chemistry Characteristic

LChS reference name `LC_WaterChemistryCharacteristic` (schema type `LC_WaterChemistryCharacteristicType`). LCCS3 `xsi:type`: `LC_WaterChemistry`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `nutrientLevel` | NutrientLevelsEnum | `eutrophic`, `mesotrophic`, `oligotrophic` |  | Nutrient Level |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
