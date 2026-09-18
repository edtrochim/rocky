---
id: characteristic:LC_ConstructionStatusCharacteristic
kind: vocab_characteristic
title: LC_ConstructionStatusCharacteristic
lchs_type: LC_ConstructionStatusCharacteristicType
lccs3_types:
- LC_ConstructionStatus
properties:
- age
- constructionStatusType
links:
- rel: allows
  id: enum:ConstructionStatusesEnum
  path: ../enums/ConstructionStatusesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_ConstructionStatusCharacteristic

Construction Status Characteristic

LChS reference name `LC_ConstructionStatusCharacteristic` (schema type `LC_ConstructionStatusCharacteristicType`). LCCS3 `xsi:type`: `LC_ConstructionStatus`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `age` | xs:decimal | min, max |  | Age |
| `constructionStatusType` | ConstructionStatusesEnum | `finished`, `inProgress`, `abandoned` |  | Construction Status Type |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
