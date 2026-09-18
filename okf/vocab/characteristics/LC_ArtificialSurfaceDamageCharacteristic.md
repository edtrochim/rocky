---
id: characteristic:LC_ArtificialSurfaceDamageCharacteristic
kind: vocab_characteristic
title: LC_ArtificialSurfaceDamageCharacteristic
lchs_type: LC_ArtificialSurfaceDamageCharacteristicType
lccs3_types:
- LC_ArtificialSurfaceDamage
properties:
- artificialSurfaceDamageType
- artificialSurfaceDamagePercentage
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_ArtificialSurfaceDamageCharacteristic

Artificial Surface Damage Characteristic

LChS reference name `LC_ArtificialSurfaceDamageCharacteristic` (schema type `LC_ArtificialSurfaceDamageCharacteristicType`). LCCS3 `xsi:type`: `LC_ArtificialSurfaceDamage`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `artificialSurfaceDamageType` | xs:string |  |  | Artificial Surface Damage Type |
| `artificialSurfaceDamagePercentage` | xs:decimal | min, max |  | Artificial Surface Damage Percentage |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
