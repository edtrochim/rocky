---
id: characteristic:LC_GrowthFormIllnessCharacteristic
kind: vocab_characteristic
title: LC_GrowthFormIllnessCharacteristic
lchs_type: LC_GrowthFormIllnessCharacteristicType
lccs3_types:
- LC_GrowthFormIllness
properties:
- growthFormIllnessType
- growthFormIllness
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_GrowthFormIllnessCharacteristic

Growth Form Illness Characteristic

LChS reference name `LC_GrowthFormIllnessCharacteristic` (schema type `LC_GrowthFormIllnessCharacteristicType`). LCCS3 `xsi:type`: `LC_GrowthFormIllness`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `growthFormIllnessType` | xs:string |  |  | Growth Form Illness Type |
| `growthFormIllness` | xs:decimal | min, max |  | Growth Form Illness Percentage |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
