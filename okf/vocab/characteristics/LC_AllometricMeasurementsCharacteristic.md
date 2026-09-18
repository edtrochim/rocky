---
id: characteristic:LC_AllometricMeasurementsCharacteristic
kind: vocab_characteristic
title: LC_AllometricMeasurementsCharacteristic
lchs_type: LC_AllometricMeasurementsCharacteristicType
lccs3_types:
- LC_AllometricMeasurements
properties:
- crownDiameter
- trunkDiameter
links: []
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_AllometricMeasurementsCharacteristic

Allometric Measurements Characteristic

LChS reference name `LC_AllometricMeasurementsCharacteristic` (schema type `LC_AllometricMeasurementsCharacteristicType`). LCCS3 `xsi:type`: `LC_AllometricMeasurements`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `crownDiameter` | xs:decimal | min, max |  | Crown Diameter |
| `trunkDiameter` | xs:decimal | min, max |  | Trunk Diameter |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
