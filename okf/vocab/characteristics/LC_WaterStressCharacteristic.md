---
id: characteristic:LC_WaterStressCharacteristic
kind: vocab_characteristic
title: LC_WaterStressCharacteristic
lchs_type: LC_WaterStressCharacteristicType
lccs3_types:
- LC_WaterStress
properties:
- waterStress
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_WaterStressCharacteristic

Water Stress Characteristic

LChS reference name `LC_WaterStressCharacteristic` (schema type `LC_WaterStressCharacteristicType`). LCCS3 `xsi:type`: `LC_WaterStress`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `waterStress` | xs:decimal | min, max |  | Water Stress |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
