---
id: standard:luml-activities
kind: standard
title: Land-use activities that masquerade as cover classes
schema: okf/0.1
status: needs_review
drafted_by: model (Claude, 2026-09-17) from the graphify graph of ISO/TS 19144-3:2024 (cd6231en) and ISO 19144-2:2023; to be reviewed by a person and then hashed
sources:
- cd6231en_doc/graphify-out/graph.json
- cd6247en_doc/graphify-out/graph.json
links:
- rel: see
  id: standard:lcml-rules
  path: lcml-rules.md
---

# Land-use activities that masquerade as cover classes

ISO/TS 19144-3 Land Use Meta Language (LUML) describes land by **function** (the purpose a piece of land
serves and the output it provides) and **activity** (what actually takes place on it in observable terms).
Five main functions: production, provision, residential, regulative, and insubstantial or other. Activities
sit under functions; both lists are extensible by registration.

Land cover systems constantly name classes by function or activity because that is what the map is for
(agricultural statistics, forest law, urban planning). The standard's position is that cover and use should
be modelled together and linked, not merged into hybrid terms that cannot be compared. In this workflow:

1. Decompose the **physical cover** the activity produces, with the standard's characteristics.
2. Record the **activity** on the class node as `land_use_hint`, from the list below.
3. Let the critic flag the class as `land_use_masquerade` so stakeholders decide whether their system is a
   cover legend, a use legend, or both.

## Common masquerades and their cover

| class name pattern | activity (LUML) | physical cover to describe |
|---|---|---|
| Pasture, grazing land, rangeland | primary production: livestock grazing | graminoids and forbs; characteristic vegetation artificiality = managed or semi-natural; grazed characteristic |
| Cropland, agriculture, arable, temporary crops | primary production: crop cultivation | herbaceous growth forms (graminoids for cereals); cultivated-and-managed characteristic with irrigation, field size, crop type, growing period |
| Permanent crops, orchard, vineyard, oil palm, coffee, banana | primary production: perennial crop cultivation | trees or shrubs; cultivated-and-managed characteristic with orchard/plantation type |
| Forest plantation, silviculture, planted forest | primary production: forestry | trees; cultivated-and-managed characteristic with tree plantation type; often even-aged |
| Mosaic of uses, mixed farming | several primary production activities | a mixed class (AND) of the component covers with proportions, or a horizontal pattern if the mosaic is a single stable feature |
| Mining, quarry, extraction site | raw material extraction | extraction surface element, bare rock or bare soil; dump site element for spoil |
| Aquaculture, fish ponds, salt pans | inland or marine harvesting | water body element, artificiality = artificial, aquaculture characteristic; salt pans: water body with salinity brine plus inorganic deposits |
| Urban area, built-up, settlement, infrastructure | residential and services | built-up surface, buildings, linear surfaces (roads, railways); non-built-up artificial surface for yards and lots |
| Urban park, sports facility, golf course | provision: recreation | graminoids with managed characteristic plus scattered trees; artificial surfaces |
| Protected area, reserve, national park | regulative: conservation | no cover of its own; describe the cover that occurs and record the instrument as framing |
| Fallow land | primary production, temporary absence | bare soil or herbaceous regrowth with a conditional temporal presence and a temporal relationship to the crop |
| Not observed, no data, clouds | none | `LC_Element` with no subtype (no data); do not decompose |

## How to record the activity

On the class node: `land_use_hint: <activity>` using the LUML activity families
(`LU_PrimaryProductionActivities`, `LU_RawEndProductionIndustryActivities`, `LU_ResidentialActivities`,
`LU_ProvisionActivities`, `LU_TransportActivities`, `LU_UtilitiesActivities`,
`LU_ConservationProtectionActivities`, `LU_RegulativeActivities`, `LU_OtherPrimaryActivities`). Keep the
hint even when the cover description is complete; the comparison step uses it to tell a translation
problem (same cover, different use words) from a real collision.

## What the 2023 edition moved

Grazing, mowing, pest control, crop fertilisation, ploughing and tree area management left ISO 19144-2 and
became ISO/TS 19144-3 activities. What stayed in the cover standard are their visible effects: the grazed,
mowed and ploughed characteristics. So "grazed grassland" is graminoids with a grazed characteristic;
"grazing land" is a use.
