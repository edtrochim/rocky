---
id: characteristic:LC_DeadStatusCharacteristic
kind: vocab_characteristic
title: LC_DeadStatusCharacteristic
lchs_type: LC_DeadStatusCharacteristicType
lccs3_types:
- LC_DeadStatus
properties:
- deadStatus
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_DeadStatusCharacteristic

Dead Status Characteristic

LChS reference name `LC_DeadStatusCharacteristic` (schema type `LC_DeadStatusCharacteristicType`). LCCS3 `xsi:type`: `LC_DeadStatus`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `deadStatus` | xs:decimal | min, max |  | Dead Status |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
