---
id: characteristic:LC_PermafrostCharacteristic
kind: vocab_characteristic
title: LC_PermafrostCharacteristic
lchs_type: LC_PermafrostCharacteristicType
lccs3_types:
- LC_Permafrost
properties:
- depth
- permafrostType
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_PermafrostCharacteristic

Permafrost Characteristic

LChS reference name `LC_PermafrostCharacteristic` (schema type `LC_PermafrostCharacteristicType`). LCCS3 `xsi:type`: `LC_Permafrost`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `depth` | xs:decimal | min, max |  | Depth |
| `permafrostType` | xs:string |  |  | Permafrost Type |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
