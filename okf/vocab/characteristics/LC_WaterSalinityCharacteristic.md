---
id: characteristic:LC_WaterSalinityCharacteristic
kind: vocab_characteristic
title: LC_WaterSalinityCharacteristic
lchs_type: LC_WaterSalinityCharacteristicType
lccs3_types:
- LC_WaterSalinity
properties:
- waterSalinity
links:
- rel: allows
  id: enum:WaterSalinityTypesEnum
  path: ../enums/WaterSalinityTypesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_WaterSalinityCharacteristic

Water Salinity Characteristic

LChS reference name `LC_WaterSalinityCharacteristic` (schema type `LC_WaterSalinityCharacteristicType`). LCCS3 `xsi:type`: `LC_WaterSalinity`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `waterSalinity` | WaterSalinityTypesEnum | `fresh`, `brackish`, `saline`, `brine` |  | Water Salinity |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
