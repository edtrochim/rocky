---
id: characteristic:LC_GrowthFormAgeCharacteristic
kind: vocab_characteristic
title: LC_GrowthFormAgeCharacteristic
lchs_type: LC_GrowthFormAgeCharacteristicType
lccs3_types:
- LC_GrowthFormAge
- LC_EvenAge
- LC_UnevenAge
properties:
- age
- unevenAge
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_GrowthFormAgeCharacteristic

Growth Form Age Characteristic

LChS reference name `LC_GrowthFormAgeCharacteristic` (schema type `LC_GrowthFormAgeCharacteristicType`). LCCS3 `xsi:type`: `LC_GrowthFormAge`, `LC_EvenAge`, `LC_UnevenAge`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `age` | xs:decimal | min, max |  | Age |
| `unevenAge` | xs:string |  |  | Uneven Age |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
