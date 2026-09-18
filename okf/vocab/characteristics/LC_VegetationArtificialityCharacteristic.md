---
id: characteristic:LC_VegetationArtificialityCharacteristic
kind: vocab_characteristic
title: LC_VegetationArtificialityCharacteristic
lchs_type: LC_VegetationArtificialityCharacteristicType
lccs3_types:
- LC_NaturalOrSeminaturalVegetation
properties:
- vegetationArtificiality
links:
- rel: allows
  id: enum:VegetationArtificialityTypesEnum
  path: ../enums/VegetationArtificialityTypesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_VegetationArtificialityCharacteristic

Vegetation Artificiality Characteristic

LChS reference name `LC_VegetationArtificialityCharacteristic` (schema type `LC_VegetationArtificialityCharacteristicType`). LCCS3 `xsi:type`: `LC_NaturalOrSeminaturalVegetation`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `vegetationArtificiality` | VegetationArtificialityTypesEnum | `natural`, `seminatural`, `naturalOrSeminatural`, `cultivated&managed`, `cultivated`, `managed` |  | Vegetation Artificiality |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
