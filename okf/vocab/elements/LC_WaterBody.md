---
id: element:LC_WaterBody
kind: vocab_element
title: LC_WaterBody
lchs_type: LC_WaterBodyType
lccs3_types:
- LC_WaterBody
properties:
- elementPresenceType
- depth
- dynamics
- position
- periodVariationDescription
- periodVariationType
- persistencePeriod
- persistenceUnits
- cover
- portioning
- density
- uOMArea
- elementHorizontalSpreading
- temporalType
- lengthOfTemporalRelationship
- lengthOfTemporalRelationshipUnits
links:
- rel: allows
  id: enum:ElementPresenceTypesEnum
  path: ../enums/ElementPresenceTypesEnum.md
- rel: allows
  id: enum:WaterIceDynamicsEnum
  path: ../enums/WaterIceDynamicsEnum.md
- rel: allows
  id: enum:WaterBodyPositionsEnum
  path: ../enums/WaterBodyPositionsEnum.md
- rel: allows
  id: enum:PeriodVariationsEnum
  path: ../enums/PeriodVariationsEnum.md
- rel: allows
  id: enum:PeriodUnitsEnum
  path: ../enums/PeriodUnitsEnum.md
- rel: allows
  id: enum:UnitsOfMeasureAreaEnum
  path: ../enums/UnitsOfMeasureAreaEnum.md
- rel: allows
  id: enum:ElementHorizontalSpreadingTypeEnum
  path: ../enums/ElementHorizontalSpreadingTypeEnum.md
- rel: allows
  id: enum:SequentialTemporalRelationshipEnum
  path: ../enums/SequentialTemporalRelationshipEnum.md
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_WaterBody

Water Body Element

LChS reference name `LC_WaterBody` (schema type `LC_WaterBodyType`). LCCS3 `xsi:type`: `LC_WaterBody`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `depth` | xs:decimal | min, max |  | Depth |
| `dynamics` | WaterIceDynamicsEnum | `flowingOrMoving`, `standing` |  | Dynamics |
| `position` | WaterBodyPositionsEnum | `aboveSurface`, `belowSurface` |  | Position |
| `periodVariationDescription` | xs:string |  |  | Period Variation Description |
| `periodVariationType` | PeriodVariationsEnum | `atmospheric`, `daily`, `seasonal`, `tidal` |  | Period Variation Type |
| `persistencePeriod` | xs:decimal | min, max |  | Persistence Period |
| `persistenceUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Persistence Period Unit |
| `cover` | xs:decimal | min, max |  | Cover |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
