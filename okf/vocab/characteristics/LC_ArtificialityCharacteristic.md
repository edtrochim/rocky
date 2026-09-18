---
id: characteristic:LC_ArtificialityCharacteristic
kind: vocab_characteristic
title: LC_ArtificialityCharacteristic
lchs_type: LC_ArtificialityCharacteristicType
lccs3_types:
- LC_Artificiality
properties:
- artificiality
links:
- rel: allows
  id: enum:ArtificialityTypesEnum
  path: ../enums/ArtificialityTypesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_ArtificialityCharacteristic

Element Artificiality Characteristic

LChS reference name `LC_ArtificialityCharacteristic` (schema type `LC_ArtificialityCharacteristicType`). LCCS3 `xsi:type`: `LC_Artificiality`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `artificiality` | ArtificialityTypesEnum | `artificial`, `natural` |  | Artificiality |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
