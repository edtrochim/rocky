---
id: element:LC_Hardpan
kind: vocab_element
title: LC_Hardpan
lchs_type: LC_HardpanType
lccs3_types:
- LC_HardPans
properties:
- elementPresenceType
- hardpanType
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
  id: enum:HardpanTypesEnum
  path: ../enums/HardpanTypesEnum.md
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
sources:
- lchs.xsd
schema: okf/0.1
---

# LC_Hardpan

Hardpan

LChS reference name `LC_Hardpan` (schema type `LC_HardpanType`). LCCS3 `xsi:type`: `LC_HardPans`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `hardpanType` | HardpanTypesEnum | `ironpan/laterite`, `petrocalcic`, `petrogypsic` |  | Hardpan Type |
| `cover` | xs:decimal | min, max |  | Cover |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
