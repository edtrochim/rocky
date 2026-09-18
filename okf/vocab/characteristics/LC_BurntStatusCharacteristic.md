---
id: characteristic:LC_BurntStatusCharacteristic
kind: vocab_characteristic
title: LC_BurntStatusCharacteristic
lchs_type: LC_BurntStatusCharacteristicType
lccs3_types:
- LC_BurntStatus
properties:
- burntStatus
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_BurntStatusCharacteristic

Burnt Status Characteristic

LChS reference name `LC_BurntStatusCharacteristic` (schema type `LC_BurntStatusCharacteristicType`). LCCS3 `xsi:type`: `LC_BurntStatus`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `burntStatus` | xs:decimal | min, max |  | Burnt Status |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
