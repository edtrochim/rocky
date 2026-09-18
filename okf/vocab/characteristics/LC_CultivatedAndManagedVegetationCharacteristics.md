---
id: characteristic:LC_CultivatedAndManagedVegetationCharacteristics
kind: vocab_characteristic
title: LC_CultivatedAndManagedVegetationCharacteristics
lchs_type: LC_CultivatedAndManagedVegetationCharacteristicsType
lccs3_types:
- LC_CultivatedAndManagedVegetation
- LC_UrbanPark
- LC_CropYield
- LC_Plantation
- LC_ForestPlantation
- LC_OrchardAndOtherPlantation
- LC_CropGrowingParameter
- LC_OverlapGrowingToReferenceCrop
- LC_CropRotation
- LC_PlantSpreadingGeometry
- LC_FieldDistribution
- LC_Irrigation
- LC_Postflooding
- LC_Rainfed
- LC_FieldSize
- LC_MechanicalErosionControl
- LC_PestControl
- LC_CropFertilization
- LC_Ploughing
- LC_TreeAreaManagementPractices
- LC_MultiTreeAreaManagementPractices
- LC_MultiTreeAreaManagementPractice
properties:
- ploughType
- frequencyMonth
- mechanicalErosionControl
- fieldSize
- irrigationType
- irrigationPercentage
- rainfedPercentage
- postfloodingPercentage
- seedingTime
- growingLength
- overlapGrowing
- overlapGrowingPeriodPercentage
- treePlantation
- orchardAndOtherPlantation
- yield
links:
- rel: allows
  id: enum:PloughTypesEnum
  path: ../enums/PloughTypesEnum.md
- rel: allows
  id: enum:IrrigationTypesEnum
  path: ../enums/IrrigationTypesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_CultivatedAndManagedVegetationCharacteristics

Cultivated & Managed Vegetation Characteristics

LChS reference name `LC_CultivatedAndManagedVegetationCharacteristics` (schema type `LC_CultivatedAndManagedVegetationCharacteristicsType`). LCCS3 `xsi:type`: `LC_CultivatedAndManagedVegetation`, `LC_UrbanPark`, `LC_CropYield`, `LC_Plantation`, `LC_ForestPlantation`, `LC_OrchardAndOtherPlantation`, `LC_CropGrowingParameter`, `LC_OverlapGrowingToReferenceCrop`, `LC_CropRotation`, `LC_PlantSpreadingGeometry`, `LC_FieldDistribution`, `LC_Irrigation`, `LC_Postflooding`, `LC_Rainfed`, `LC_FieldSize`, `LC_MechanicalErosionControl`, `LC_PestControl`, `LC_CropFertilization`, `LC_Ploughing`, `LC_TreeAreaManagementPractices`, `LC_MultiTreeAreaManagementPractices`, `LC_MultiTreeAreaManagementPractice`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `ploughType` | PloughTypesEnum | `manual`, `manualOrAnimal`, `mechanical` |  | Plough Type |
| `frequencyMonth` | xs:decimal | min, max |  | Frequency (Month) |
| `mechanicalErosionControl` | PloughTypesEnum | `manual`, `manualOrAnimal`, `mechanical` |  | Mechanical Erosion Control |
| `fieldSize` | xs:decimal | min, max |  | Field Size |
| `irrigationType` | IrrigationTypesEnum | `surface`, `sprinkler`, `drip` |  | Irrigation Type |
| `irrigationPercentage` | xs:decimal | min, max |  | Irrigation Percentage |
| `rainfedPercentage` | xs:decimal | min, max |  | Rainfed Percentage |
| `postfloodingPercentage` | xs:decimal | min, max |  | Postflooding Percentage |
| `seedingTime` | xs:decimal | min, max |  | Seeding Time |
| `growingLength` | xs:decimal | min, max |  | Growing Length |
| `overlapGrowing` | xs:decimal | min, max |  | Overlap Growing |
| `overlapGrowingPeriodPercentage` | xs:decimal | min, max |  | Overlap Growing Period |
| `treePlantation` | xs:string |  |  | Tree Plantation |
| `orchardAndOtherPlantation` | xs:string |  |  | Orchard & Other Plantation |
| `yield` | xs:decimal | min, max |  | Crop Yield |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
