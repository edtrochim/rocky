---
id: characteristic:LC_MowedCharacteristic
kind: vocab_characteristic
title: LC_MowedCharacteristic
lchs_type: LC_MowedCharacteristicType
lccs3_types: []
properties:
- mowed
links:
- rel: allows
  id: enum:BooleanEnum
  path: ../enums/BooleanEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_MowedCharacteristic

Mowed Characteristic

LChS reference name `LC_MowedCharacteristic` (schema type `LC_MowedCharacteristicType`). No LCCS3 equivalent.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `mowed` | BooleanEnum | `true`, `false` |  | Mowed |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
