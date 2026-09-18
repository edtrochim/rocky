---
id: characteristic:LC_VegetationDamageCharacteristic
kind: vocab_characteristic
title: LC_VegetationDamageCharacteristic
lchs_type: LC_VegetationDamageCharacteristicType
lccs3_types:
- LC_VegetationDamage
properties:
- damageType
- damage
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_VegetationDamageCharacteristic

Vegetation Damage Characteristic

LChS reference name `LC_VegetationDamageCharacteristic` (schema type `LC_VegetationDamageCharacteristicType`). LCCS3 `xsi:type`: `LC_VegetationDamage`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `damageType` | xs:string |  |  | Damage Type |
| `damage` | xs:decimal | min, max |  | Damage Percentage |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
