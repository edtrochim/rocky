---
id: element:LC_Shrub
kind: vocab_element
title: LC_Shrub
lchs_type: LC_ShrubType
lccs3_types:
- LC_Shrubs
properties:
- elementPresenceType
- cover
- height
- depth
- woodyLeafPhenology
- evergreenPercentage
- deciduousPercentage
- deciduousStart
- deciduousLength
- woodyLeafType
- broadLeafPercentage
- needleLeafPercentage
- aphyllousPercentage
- leafArragement
- leafShape
- leafVenation
- leafAspectType
- leafCharacterSizeType
- portioning
- density
- uOMArea
- elementHorizontalSpreading
- temporalType
- lengthOfTemporalRelationship
- lengthOfTemporalRelationshipUnits
- lifeFormSpecialization
links:
- rel: allows
  id: enum:ElementPresenceTypesEnum
  path: ../enums/ElementPresenceTypesEnum.md
- rel: allows
  id: enum:WoodyLeafPhenologiesEnum
  path: ../enums/WoodyLeafPhenologiesEnum.md
- rel: allows
  id: enum:LeafTypesEnum
  path: ../enums/LeafTypesEnum.md
- rel: allows
  id: enum:LeafArrangementsEnum
  path: ../enums/LeafArrangementsEnum.md
- rel: allows
  id: enum:LeafShapesEnum
  path: ../enums/LeafShapesEnum.md
- rel: allows
  id: enum:LeafVenationsEnum
  path: ../enums/LeafVenationsEnum.md
- rel: allows
  id: enum:LeafAspectsEnum
  path: ../enums/LeafAspectsEnum.md
- rel: allows
  id: enum:LeafCharacterSizeTypesEnum
  path: ../enums/LeafCharacterSizeTypesEnum.md
- rel: allows
  id: enum:UnitsOfMeasureAreaEnum
  path: ../enums/UnitsOfMeasureAreaEnum.md
- rel: allows
  id: enum:ElementHorizontalSpreadingTypeEnum
  path: ../enums/ElementHorizontalSpreadingTypeEnum.md
- rel: allows
  id: enum:SequentialTemporalRelationshipEnum
  path: ../enums/SequentialTemporalRelationshipEnum.md
- rel: allows
  id: enum:PeriodUnitsEnum
  path: ../enums/PeriodUnitsEnum.md
- rel: allows
  id: enum:LifeFormSpecializationTypesEnum
  path: ../enums/LifeFormSpecializationTypesEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_Shrub

Woody Growth Form Element of Shrub Subtype

LChS reference name `LC_Shrub` (schema type `LC_ShrubType`). LCCS3 `xsi:type`: `LC_Shrubs`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `cover` | xs:decimal | min, max |  | Cover |
| `height` | xs:decimal | min, max |  | Height |
| `depth` | xs:decimal | min, max |  | Depth |
| `woodyLeafPhenology` | WoodyLeafPhenologiesEnum | `Deciduous`, `Evergreen` |  | Woody Leaf Phenology |
| `evergreenPercentage` | xs:decimal | min, max |  | Evergreen Percentage |
| `deciduousPercentage` | xs:decimal | min, max |  | Deciduous Percentage |
| `deciduousStart` | xs:decimal | min, max |  | Deciduous Start |
| `deciduousLength` | xs:decimal | min, max |  | Deciduous Length |
| `woodyLeafType` | LeafTypesEnum | `Aphyllous`, `NeedleLeaf`, `BroadLeaf` |  | Woody Leaf Type |
| `broadLeafPercentage` | xs:decimal | min, max |  | Broad Leaf Percentage |
| `needleLeafPercentage` | xs:decimal | min, max |  | Needle Leaf Percentage |
| `aphyllousPercentage` | xs:decimal | min, max |  | Aphyllous Percentage |
| `leafArragement` | LeafArrangementsEnum | `alternate`, `helical`, `opposite`, `whorled` |  | Leaf Arrangement |
| `leafShape` | LeafShapesEnum | `acicular`, `acuminate`, `aristate`, `bipinnate`, `cordate`, `cuneate`, `deltoid`, `digitate`, `elliptic`, `falcate`, `flabellate`, `hastate` … (40 values, see enum) |  | Leaf Shape |
| `leafVenation` | LeafVenationsEnum | `dichotomous`, `palmateReticulate`, `parallelExpandedLeaf`, `parallelLinearLeaf`, `pinnateReticulate` |  | Leaf Venation |
| `leafAspectType` | LeafAspectsEnum | `sclerophyllous`, `soft_leaved`, `succulent` |  | Leaf Aspect Type |
| `leafCharacterSizeType` | LeafCharacterSizeTypesEnum | `large_leaf`, `medium_leaf`, `small_leaf` |  | Leaf Character Size Type |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |
| `lifeFormSpecialization` | LifeFormSpecializationTypesEnum | `bamboos`, `climbers`, `eppphytes`, `stem_succulents`, `tuft_plants`, `arboreal_giant_herbs` |  | Life Form Specialization |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
