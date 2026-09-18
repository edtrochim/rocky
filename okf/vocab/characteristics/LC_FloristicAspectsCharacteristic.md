---
id: characteristic:LC_FloristicAspectsCharacteristic
kind: vocab_characteristic
title: LC_FloristicAspectsCharacteristic
lchs_type: LC_FloristicAspectsCharacteristicType
lccs3_types:
- LC_FloristicAspect
- LC_FloristicAspectSpecies
- LC_SinglePlantSpecies
- LC_GroupOfPlantSpecies
properties:
- speciesName
- singlePlantSpeciesType
- groupOfPlantSpeciesType
links:
- rel: allows
  id: enum:SinglePlantSpeciesTypesEnum
  path: ../enums/SinglePlantSpeciesTypesEnum.md
- rel: allows
  id: enum:GroupOfPlantSpeciesTypesEnum
  path: ../enums/GroupOfPlantSpeciesTypesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_FloristicAspectsCharacteristic

Floristic Aspects Characteristic

LChS reference name `LC_FloristicAspectsCharacteristic` (schema type `LC_FloristicAspectsCharacteristicType`). LCCS3 `xsi:type`: `LC_FloristicAspect`, `LC_FloristicAspectSpecies`, `LC_SinglePlantSpecies`, `LC_GroupOfPlantSpecies`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `speciesName` | xs:string |  |  | Species Name |
| `singlePlantSpeciesType` | SinglePlantSpeciesTypesEnum | `dominant`, `mostFrequent` |  | Single Plant Species Type |
| `groupOfPlantSpeciesType` | GroupOfPlantSpeciesTypesEnum | `statisticallyDerivedPlantGroup`, `nonStatisticallyDerivedPlantGroup` |  | Group Of Plant Species Type |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
