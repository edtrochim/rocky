---
id: characteristic:LC_GrazedCharacteristic
kind: vocab_characteristic
title: LC_GrazedCharacteristic
lchs_type: LC_GrazedCharacteristicType
lccs3_types:
- LC_Grazing
- LC_GrazingAnimalType
properties:
- intensity
- animalType
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_GrazedCharacteristic

Grazed Characteristic

LChS reference name `LC_GrazedCharacteristic` (schema type `LC_GrazedCharacteristicType`). LCCS3 `xsi:type`: `LC_Grazing`, `LC_GrazingAnimalType`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `intensity` | xs:decimal | min, max |  | Intensity |
| `animalType` | xs:string |  |  | Animal Type |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
