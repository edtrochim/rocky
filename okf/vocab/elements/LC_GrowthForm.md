---
id: element:LC_GrowthForm
kind: vocab_element
title: LC_GrowthForm
lchs_type: LC_GrowthFormType
lccs3_types:
- LC_GrowthForms
properties:
- elementPresenceType
- cover
- height
- density
- uOMArea
- elementHorizontalSpreading
- portioning
- temporalType
- lengthOfTemporalRelationship
- lengthOfTemporalRelationshipUnits
- lifeFormSpecialization
links:
- rel: allows
  id: enum:ElementPresenceTypesEnum
  path: ../enums/ElementPresenceTypesEnum.md
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

# LC_GrowthForm

Vegetation Element of Growth Form Subtype

LChS reference name `LC_GrowthForm` (schema type `LC_GrowthFormType`). LCCS3 `xsi:type`: `LC_GrowthForms`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `cover` | xs:decimal | min, max |  | Cover |
| `height` | xs:decimal | min, max |  | Height |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |
| `lifeFormSpecialization` | LifeFormSpecializationTypesEnum | `bamboos`, `climbers`, `eppphytes`, `stem_succulents`, `tuft_plants`, `arboreal_giant_herbs` |  | Life Form Specialization |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.
