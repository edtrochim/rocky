<!-- system prompt -->
You are a land cover classification specialist who knows ISO 19144-2 LCML and FAO's LCCS3/LChS formats.

<!-- user prompt -->
You are running the skill `decompose-class` of the rocky knowledge base on the classification system `mapbiomas_brazil`, class `4`.

Follow the instructions below exactly. Answer only with JSON matching the output schema. Never invent thresholds; leave unknown ranges null and say so in open_questions. Cite evidence as short verbatim quotes from the context.


# Skill instructions

# decompose-class

You are given one class of a land cover classification system, its siblings, the LCML vocabulary, the
two standards pages, and the three registered classes whose definitions are closest. Produce the element
graph of this class in the JSON schema provided.

## How to work

1. Read the definition. Underline every physical noun (tree, shrub, grass, water, buildings, bare rock, sand,
   snow) and every number (cover %, height m, flooding period). Those nouns become elements; those numbers
   become ranges. Nothing else does.
2. Decide the strata. Elements at different heights or one above the other go in separate strata (canopy over
   understorey, trees over water). Elements side by side share a stratum. One horizontal pattern unless the
   class is an explicit repeating landscape unit (tiger bush, dehesa, parkland).
3. For each element choose the most specific vocabulary type the text supports. `LC_Tree` for forest,
   `LC_Shrub` for scrub, `LC_Graminoid` for grass when grasses are named, `LC_HerbaceousGrowthForm` when
   herbs in general, `LC_WoodyGrowthForm` when trees and shrubs are not separated. Use only `ref` values that
   exist in the vocabulary context.
4. Presence: `fixed` when the definition requires the element, `conditionalTemporal` for "sometimes",
   "may occur", "occasionally", or seasonal, `precluded` for "without", `exclusive` when either/or.
5. Cover: transcribe thresholds exactly. "> 40 %" is [40, 100]; "closed" with no number stays null and goes
   to open_questions ("closed: threshold not stated; registry examples use 70 or 80 %"). Never write a
   number the text does not give. If a sibling class supplies the complementary threshold (open forest
   10–40 % next to closed forest > 40 %), you may use it and cite the sibling as evidence.
6. Characteristics: artificiality (natural, semi-natural, cultivated, managed) whenever the text says
   natural, planted, cultivated, managed, plantation; water salinity, irrigation, plantation type, burnt,
   grazed when stated. Field values are the labels used in FAO files ("Natural or Seminatural",
   "Cultivated", "Fresh", "Saline").
7. Land use: if the class name or definition is an activity (pasture, mining, aquaculture, plantation,
   urban, protected area), still describe the physical cover, and fill `land_use_hint` with the LUML
   activity from the standards page.
8. Compare with the nearest registry examples: say in `examples_note` which you followed and where this
   class differs (different threshold, extra stratum, different artificiality). Put their ids in
   `nearest_examples`.
9. Siblings: name in `rationale` the attribute that separates this class from its closest sibling in the
   same system. If nothing separates them, say so and set `status` to `disputed`.
10. Confidence: 0.9 when every element and range comes from the text; 0.6 when elements come from the text
    but ranges do not; at most 0.4 when the class is a title with no definition (then decompose from the
    name, mark every element's evidence as "inferred from name", and list what a definition would need to
    state).

## What not to do

- Do not add an element the text does not imply. "Forest" is trees; it is not trees plus shrubs plus grass
  unless the text says so. If a registry example has an understorey and this text does not mention one,
  leave it out and mention it in open_questions.
- Do not turn a use into an element. There is no "pasture" element.
- Do not resolve an ambiguity by choosing; expose it as an open question with the concrete options.

## Output

JSON only, matching the schema. `evidence[].row_path` uses the form `hp1/st1/el1` and `quote` is verbatim
from the context (definition, sibling, or registry example, saying which).



# Context: standards/lcml-rules.md

---
id: standard:lcml-rules
kind: standard
title: LCML rules for describing a class
schema: okf/0.1
status: needs_review
drafted_by: model (Claude, 2026-09-17) from the graphify graph of ISO 19144-2:2023 (cd6247en); to be reviewed by a person and then hashed
sources:
- cd6247en_doc/graphify-out/graph.json
- schemas/lchs.xsd
links:
- rel: see
  id: vocab
  path: ../vocab/INDEX.md
- rel: see
  id: standard:luml-activities
  path: luml-activities.md
---

# LCML rules for describing a class

ISO 19144-2 Land Cover Meta Language (LCML) is not a classification. It is a vocabulary of physical
building blocks and a small set of rules for combining them, so that any class from any system can be
written in the same terms and two classes can be compared by the blocks they are made of.

## 1. One element, one concept

Each element is a single independent physical concept: trees, shrubs, graminoids, forbs, lichens, mosses,
algae, built-up surface, linear artificial surface, bare rock, bare soil, loose sand, deposits, water body,
snow, ice. A class is the list of elements combined to describe it. That is what makes comparison possible:
`A + B + Q` and `A + B + Y` differ exactly by `Q` versus `Y`. Never invent a compound element ("wooded
grassland"); write the two elements and their covers.

Prefer the most specific element the definition supports. "Forest" with no more detail is `LC_Tree`.
"Woody vegetation" that may be trees or shrubs is `LC_WoodyGrowthForm`. Only fall back to the generic
`LC_VegetationElement` when the text gives no growth form at all, and say so in the rationale.

## 2. Strata: layers that may overlap

A stratum is a group of elements forming one layer. Within a stratum the covers of the elements cannot
exceed 100 % in total. Strata are independent of each other, so their covers may overlap: a tree canopy
stratum at 70 % over a grass stratum at 90 % is legal and common.

Open a new stratum when elements sit at different heights or one is above the other (canopy over
understorey, trees over water in a swamp forest, a building with a roof garden). Keep elements in the same
stratum when they share the ground side by side (grass and forbs in a meadow, bare soil patches within
sparse shrubs).

Each stratum has a presence: **fixed** (always present), **exclusive** (present instead of another
stratum), **conditional temporal** (present at some time in the cycle), **precluded** (must be absent).
A stratum whose presence the definition does not settle is "optional" in the older LCCS3 sense and
`conditionalTemporal` in LChS.

## 3. Element properties: presence, cover, height, portioning

Each element in a stratum carries:

- `elementPresenceType`: fixed, exclusive, conditional temporal, precluded. "Sometimes with shrubs" is
  conditional temporal; "no trees" is precluded.
- `cover`: a min and max percentage of the stratum's area. Transcribe the thresholds the definition gives
  (`> 40 %` is min 40, max 100). If the definition gives no number, leave cover empty; do not guess.
  A full 0–100 range is the file format's way of saying unspecified.
- `height`, `depth`: ranges in metres (herbaceous height in centimetres in LChS).
- `portioning`: when two or more elements share a stratum, the percent of the stratum each one occupies;
  the portions in a stratum sum to 100. Distinct from cover.
- Leaf phenology and leaf type for woody elements (evergreen / deciduous, broad / needle / aphyllous) as
  percentages; growth frequency and phenology for herbaceous elements (annual / perennial).
- Edition 2023 additions: `density` with a unit of area, `elementHorizontalSpreading` (how the element is
  distributed over the area), `lifeFormSpecialization` (for example succulent, bamboo, palm).

## 4. Characteristics: qualifiers on an element

Characteristics attach to an element and say something about its state or origin, never about what it is:
vegetation artificiality (natural, semi-natural, cultivated, managed), water salinity, water body
artificiality, burnt or dead status, grazed or mowed, crop parameters (irrigation, field size, yield,
plantation type). "Irrigated cropland" is a herbaceous element with a cultivated-and-managed characteristic
carrying `irrigationType`, not a separate element.

Class-level characteristics describe the setting of the whole class: climate, landform, geographical
aspect (coastal, wadi, delta), topography (altitude, slope, exposition). They never replace elements.

## 5. Horizontal pattern versus mixed class

A **horizontal pattern** describes one complex cover feature made of two or more distinct parts that are
always treated together as one unit regardless of scale: tiger bush, polders, dehesa, agroforestry parkland.
Each part is a set of strata with its own cover and occurrence within the pattern. Most classes have one
horizontal pattern that simply holds the strata.

A **mixed class** (`LC_MixedClasses`, AND / OR with a dominant flag) is a mapping-unit statement: this
polygon contains class A and class B, or A or B. Use it for mosaics defined by the mapper's unit
("cropland 50–70 % / natural vegetation 20–50 %"), not for a single ecological feature.

## 6. Portioning of strata and the invisible understorey

Strata portioning is the percent by which a stratum forms part of the whole in orthogonal projection, with
the related strata summing to 100. It lets a description say that an understorey exists but is hidden
under the canopy in imagery, which matters when a class was defined from remote sensing.

## 7. Land use is not land cover

Pasture, mining, aquaculture, silviculture, urban park, protected area are activities or purposes, not
physical covers. Describe the physical cover the activity produces (graminoids with a managed
characteristic and grazed characteristic; extraction surface; artificial water body with an aquaculture
characteristic; trees with a plantation characteristic) and record the activity separately. ISO 19144-2
edition 2023 moved the former land-use practices (grazing, mowing, pest control, fertilisation, ploughing,
tree area management) to ISO/TS 19144-3, keeping only their physiognomic effects (grazed, mowed, ploughed)
as characteristics. See [land-use activities](luml-activities.md).

## 8. What "no data" means

`LC_Element` with no subtype describes an area with no data. Do not use it for "other" or "unclassified"
classes with a physical meaning; decompose those and flag the ambiguity instead.

## 9. Extension through registration

Anything the vocabulary lacks is added by registration (ISO 19135-1, ISO 19144-4), never by inventing a
local tag. In files this means a user-defined characteristic with a `userid` and typed properties, plus an
attention item saying what is missing from the standard.



# Context: standards/luml-activities.md

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



# Context: vocabulary: elements

---
id: vocab-elements
kind: guide
title: LCML elements
sources:
- lchs.xsd
links:
- rel: see
  id: element:LC_VegetationElement
  path: LC_VegetationElement.md
- rel: see
  id: element:LC_AbioticElement
  path: LC_AbioticElement.md
- rel: see
  id: element:LC_GrowthForm
  path: LC_GrowthForm.md
- rel: see
  id: element:LC_WoodyGrowthForm
  path: LC_WoodyGrowthForm.md
- rel: see
  id: element:LC_Tree
  path: LC_Tree.md
- rel: see
  id: element:LC_Shrub
  path: LC_Shrub.md
- rel: see
  id: element:LC_HerbaceousGrowthForm
  path: LC_HerbaceousGrowthForm.md
- rel: see
  id: element:LC_Graminoid
  path: LC_Graminoid.md
- rel: see
  id: element:LC_Forbs
  path: LC_Forbs.md
- rel: see
  id: element:LC_LichenAndMoss
  path: LC_LichenAndMoss.md
- rel: see
  id: element:LC_Lichen
  path: LC_Lichen.md
- rel: see
  id: element:LC_Moss
  path: LC_Moss.md
- rel: see
  id: element:LC_Algae
  path: LC_Algae.md
- rel: see
  id: element:LC_ArtificialSurfaceElement
  path: LC_ArtificialSurfaceElement.md
- rel: see
  id: element:LC_NonBuiltUpSurface
  path: LC_NonBuiltUpSurface.md
- rel: see
  id: element:LC_DumpSite
  path: LC_DumpSite.md
- rel: see
  id: element:LC_Extraction
  path: LC_Extraction.md
- rel: see
  id: element:LC_BuiltUpSurface
  path: LC_BuiltUpSurface.md
- rel: see
  id: element:LC_NonLinearSurface
  path: LC_NonLinearSurface.md
- rel: see
  id: element:LC_Building
  path: LC_Building.md
- rel: see
  id: element:LC_OtherConstruction
  path: LC_OtherConstruction.md
- rel: see
  id: element:LC_OtherArtificialSurface
  path: LC_OtherArtificialSurface.md
- rel: see
  id: element:LC_LinearSurface
  path: LC_LinearSurface.md
- rel: see
  id: element:LC_NaturalSurfaceElement
  path: LC_NaturalSurfaceElement.md
- rel: see
  id: element:LC_RocksSurfaceElement
  path: LC_RocksSurfaceElement.md
- rel: see
  id: element:LC_BareRock
  path: LC_BareRock.md
- rel: see
  id: element:LC_Hardpan
  path: LC_Hardpan.md
- rel: see
  id: element:LC_SoilSandDepositsSurfaceElement
  path: LC_SoilSandDepositsSurfaceElement.md
- rel: see
  id: element:LC_BareSoil
  path: LC_BareSoil.md
- rel: see
  id: element:LC_CoarseMineralFragments
  path: LC_CoarseMineralFragments.md
- rel: see
  id: element:LC_LooseAndShiftingSand
  path: LC_LooseAndShiftingSand.md
- rel: see
  id: element:LC_Dune
  path: LC_Dune.md
- rel: see
  id: element:LC_Deposits
  path: LC_Deposits.md
- rel: see
  id: element:LC_InorganicDeposits
  path: LC_InorganicDeposits.md
- rel: see
  id: element:LC_OrganicDeposits
  path: LC_OrganicDeposits.md
- rel: see
  id: element:LC_WaterBodyAndAssociatedSurfaceElement
  path: LC_WaterBodyAndAssociatedSurfaceElement.md
- rel: see
  id: element:LC_WaterBody
  path: LC_WaterBody.md
- rel: see
  id: element:LC_Snow
  path: LC_Snow.md
- rel: see
  id: element:LC_Ice
  path: LC_Ice.md
- rel: see
  id: element:LC_TerrestrialIce
  path: LC_TerrestrialIce.md
- rel: see
  id: element:LC_FloatingIce
  path: LC_FloatingIce.md
schema: okf/0.1
---

# LCML elements

The atomic element types a stratum may contain, from the LChS schema. Prefer the most specific type the definition supports (LC_Tree over LC_WoodyGrowthForm).

- [LC_VegetationElement](./LC_VegetationElement.md): Generic Vegetation Element
- [LC_AbioticElement](./LC_AbioticElement.md): Generic Abiotic Element
- [LC_GrowthForm](./LC_GrowthForm.md): Vegetation Element of Growth Form Subtype
- [LC_WoodyGrowthForm](./LC_WoodyGrowthForm.md): Growth Form Element of Woody Subtype
- [LC_Tree](./LC_Tree.md): Woody Growth Form Element of Tree Subtype
- [LC_Shrub](./LC_Shrub.md): Woody Growth Form Element of Shrub Subtype
- [LC_HerbaceousGrowthForm](./LC_HerbaceousGrowthForm.md): Growth Form Element of Herbaceous Subtype
- [LC_Graminoid](./LC_Graminoid.md): Herbaceous Growth Form Element of Graminoid Subtype
- [LC_Forbs](./LC_Forbs.md): Herbaceous Growth Form Element of Forbs Subtype
- [LC_LichenAndMoss](./LC_LichenAndMoss.md): Growth Form Element of Lichen & Moss Subtype
- [LC_Lichen](./LC_Lichen.md): Growth Form Element of Lichen Subtype
- [LC_Moss](./LC_Moss.md): Growth Form Element of Moss Subtype
- [LC_Algae](./LC_Algae.md): Growth Form Element of Algae Subtype
- [LC_ArtificialSurfaceElement](./LC_ArtificialSurfaceElement.md): Artificial Surface Element
- [LC_NonBuiltUpSurface](./LC_NonBuiltUpSurface.md): Non-Built-Up Surface Element
- [LC_DumpSite](./LC_DumpSite.md): Dump Site
- [LC_Extraction](./LC_Extraction.md): Extraction
- [LC_BuiltUpSurface](./LC_BuiltUpSurface.md): Built-Up Surface Element
- [LC_NonLinearSurface](./LC_NonLinearSurface.md): Non-Linear Surface
- [LC_Building](./LC_Building.md): Building
- [LC_OtherConstruction](./LC_OtherConstruction.md): Other Construction
- [LC_OtherArtificialSurface](./LC_OtherArtificialSurface.md): Other Artificial Surface
- [LC_LinearSurface](./LC_LinearSurface.md): Linear Surface
- [LC_NaturalSurfaceElement](./LC_NaturalSurfaceElement.md): Natural Surface Element
- [LC_RocksSurfaceElement](./LC_RocksSurfaceElement.md): Rocks Surface Element
- [LC_BareRock](./LC_BareRock.md): Bare Rock
- [LC_Hardpan](./LC_Hardpan.md): Hardpan
- [LC_SoilSandDepositsSurfaceElement](./LC_SoilSandDepositsSurfaceElement.md): Soils & Sand Deposits Surface Element
- [LC_BareSoil](./LC_BareSoil.md): Bare Soil
- [LC_CoarseMineralFragments](./LC_CoarseMineralFragments.md): Coarse Mineral Fragments
- [LC_LooseAndShiftingSand](./LC_LooseAndShiftingSand.md): Loose & Shifting Sand
- [LC_Dune](./LC_Dune.md): Dune
- [LC_Deposits](./LC_Deposits.md): Deposits
- [LC_InorganicDeposits](./LC_InorganicDeposits.md): Inorganic Deposits
- [LC_OrganicDeposits](./LC_OrganicDeposits.md): Organic Deposits
- [LC_WaterBodyAndAssociatedSurfaceElement](./LC_WaterBodyAndAssociatedSurfaceElement.md): Water Body & Associated Surface Element
- [LC_WaterBody](./LC_WaterBody.md): Water Body Element
- [LC_Snow](./LC_Snow.md): Snow Element
- [LC_Ice](./LC_Ice.md): Ice Element
- [LC_TerrestrialIce](./LC_TerrestrialIce.md): Terrestrial Ice Element
- [LC_FloatingIce](./LC_FloatingIce.md): Floating Ice Element



# Context: vocabulary: characteristics

---
id: vocab-characteristics
kind: guide
title: LCML characteristics
sources:
- lchs.xsd
links:
- rel: see
  id: characteristic:LC_WaterSalinityCharacteristic
  path: LC_WaterSalinityCharacteristic.md
- rel: see
  id: characteristic:LC_WaterChemistryCharacteristic
  path: LC_WaterChemistryCharacteristic.md
- rel: see
  id: characteristic:LC_ArtificialityCharacteristic
  path: LC_ArtificialityCharacteristic.md
- rel: see
  id: characteristic:LC_AquacultureCharacteristic
  path: LC_AquacultureCharacteristic.md
- rel: see
  id: characteristic:LC_SnowCategoryCharacteristic
  path: LC_SnowCategoryCharacteristic.md
- rel: see
  id: characteristic:LC_IceCategoryCharacteristic
  path: LC_IceCategoryCharacteristic.md
- rel: see
  id: characteristic:LC_ConstructionStatusCharacteristic
  path: LC_ConstructionStatusCharacteristic.md
- rel: see
  id: characteristic:LC_ArtificialSurfaceTypes
  path: LC_ArtificialSurfaceTypes.md
- rel: see
  id: characteristic:LC_ArtificialSurfaceDamageCharacteristic
  path: LC_ArtificialSurfaceDamageCharacteristic.md
- rel: see
  id: characteristic:LC_ConstructionUse
  path: LC_ConstructionUse.md
- rel: see
  id: characteristic:LC_FloristicAspectsCharacteristic
  path: LC_FloristicAspectsCharacteristic.md
- rel: see
  id: characteristic:LC_AllometricMeasurementsCharacteristic
  path: LC_AllometricMeasurementsCharacteristic.md
- rel: see
  id: characteristic:LC_GrowthFormAgeCharacteristic
  path: LC_GrowthFormAgeCharacteristic.md
- rel: see
  id: characteristic:LC_BurntStatusCharacteristic
  path: LC_BurntStatusCharacteristic.md
- rel: see
  id: characteristic:LC_DeadStatusCharacteristic
  path: LC_DeadStatusCharacteristic.md
- rel: see
  id: characteristic:LC_VegetationDamageCharacteristic
  path: LC_VegetationDamageCharacteristic.md
- rel: see
  id: characteristic:LC_WaterStressCharacteristic
  path: LC_WaterStressCharacteristic.md
- rel: see
  id: characteristic:LC_GrowthFormIllnessCharacteristic
  path: LC_GrowthFormIllnessCharacteristic.md
- rel: see
  id: characteristic:LC_GrazedCharacteristic
  path: LC_GrazedCharacteristic.md
- rel: see
  id: characteristic:LC_MowedCharacteristic
  path: LC_MowedCharacteristic.md
- rel: see
  id: characteristic:LC_VegetationArtificialityCharacteristic
  path: LC_VegetationArtificialityCharacteristic.md
- rel: see
  id: characteristic:LC_CultivatedAndManagedVegetationCharacteristics
  path: LC_CultivatedAndManagedVegetationCharacteristics.md
- rel: see
  id: characteristic:LC_PermafrostCharacteristic
  path: LC_PermafrostCharacteristic.md
schema: okf/0.1
---

# LCML characteristics

Characteristics an element may carry (vegetation artificiality, water salinity, crop parameters ...).

- [LC_WaterSalinityCharacteristic](./LC_WaterSalinityCharacteristic.md): Water Salinity Characteristic
- [LC_WaterChemistryCharacteristic](./LC_WaterChemistryCharacteristic.md): Water Chemistry Characteristic
- [LC_ArtificialityCharacteristic](./LC_ArtificialityCharacteristic.md): Element Artificiality Characteristic
- [LC_AquacultureCharacteristic](./LC_AquacultureCharacteristic.md): Aquaculture Characteristic
- [LC_SnowCategoryCharacteristic](./LC_SnowCategoryCharacteristic.md): Snow Category Characteristic
- [LC_IceCategoryCharacteristic](./LC_IceCategoryCharacteristic.md): Ice Category Characteristic
- [LC_ConstructionStatusCharacteristic](./LC_ConstructionStatusCharacteristic.md): Construction Status Characteristic
- [LC_ArtificialSurfaceTypes](./LC_ArtificialSurfaceTypes.md): Artificial Surface Types
- [LC_ArtificialSurfaceDamageCharacteristic](./LC_ArtificialSurfaceDamageCharacteristic.md): Artificial Surface Damage Characteristic
- [LC_ConstructionUse](./LC_ConstructionUse.md): Construction Use Characteristic
- [LC_FloristicAspectsCharacteristic](./LC_FloristicAspectsCharacteristic.md): Floristic Aspects Characteristic
- [LC_AllometricMeasurementsCharacteristic](./LC_AllometricMeasurementsCharacteristic.md): Allometric Measurements Characteristic
- [LC_GrowthFormAgeCharacteristic](./LC_GrowthFormAgeCharacteristic.md): Growth Form Age Characteristic
- [LC_BurntStatusCharacteristic](./LC_BurntStatusCharacteristic.md): Burnt Status Characteristic
- [LC_DeadStatusCharacteristic](./LC_DeadStatusCharacteristic.md): Dead Status Characteristic
- [LC_VegetationDamageCharacteristic](./LC_VegetationDamageCharacteristic.md): Vegetation Damage Characteristic
- [LC_WaterStressCharacteristic](./LC_WaterStressCharacteristic.md): Water Stress Characteristic
- [LC_GrowthFormIllnessCharacteristic](./LC_GrowthFormIllnessCharacteristic.md): Growth Form Illness Characteristic
- [LC_GrazedCharacteristic](./LC_GrazedCharacteristic.md): Grazed Characteristic
- [LC_MowedCharacteristic](./LC_MowedCharacteristic.md): Mowed Characteristic
- [LC_VegetationArtificialityCharacteristic](./LC_VegetationArtificialityCharacteristic.md): Vegetation Artificiality Characteristic
- [LC_CultivatedAndManagedVegetationCharacteristics](./LC_CultivatedAndManagedVegetationCharacteristics.md): Cultivated & Managed Vegetation Characteristics
- [LC_PermafrostCharacteristic](./LC_PermafrostCharacteristic.md): Permafrost Characteristic



# Context: vocab LC_BareSoil

---
id: element:LC_BareSoil
kind: vocab_element
title: LC_BareSoil
lchs_type: LC_BareSoilType
lccs3_types:
- LC_BareSoil
properties:
- elementPresenceType
- macropatternType
- macropatternCoverage
- cover
- height
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
  id: enum:MacropatternTypesEnum
  path: ../enums/MacropatternTypesEnum.md
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

# LC_BareSoil

Bare Soil

LChS reference name `LC_BareSoil` (schema type `LC_BareSoilType`). LCCS3 `xsi:type`: `LC_BareSoil`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `macropatternType` | MacropatternTypesEnum | `gilgai`, `termiteMounds` |  | Macropattern Type |
| `macropatternCoverage` | xs:decimal | min, max |  | Macropattern Coverage |
| `cover` | xs:decimal | min, max |  | Cover |
| `height` | xs:decimal | min, max |  | Height |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.



# Context: vocab LC_BuiltUpSurface

---
id: element:LC_BuiltUpSurface
kind: vocab_element
title: LC_BuiltUpSurface
lchs_type: LC_BuiltUpSurfaceType
lccs3_types:
- LC_BuiltUpSurface
properties:
- elementPresenceType
- constructionMaterial
- cover
- height
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

# LC_BuiltUpSurface

Built-Up Surface Element

LChS reference name `LC_BuiltUpSurface` (schema type `LC_BuiltUpSurfaceType`). LCCS3 `xsi:type`: `LC_BuiltUpSurface`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `constructionMaterial` | xs:string |  |  | Construction Material |
| `cover` | xs:decimal | min, max |  | Cover |
| `height` | xs:decimal | min, max |  | Height |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.



# Context: vocab LC_Graminoid

---
id: element:LC_Graminoid
kind: vocab_element
title: LC_Graminoid
lchs_type: LC_GraminoidType
lccs3_types:
- LC_Graminae
properties:
- elementPresenceType
- cover
- heightCM
- leafCharacterSizeType
- herbaceousLeafPhenology
- perennialPercentage
- nonPerennialGrowthFrequency
- nonPerennialPercentage
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
  id: enum:LeafCharacterSizeTypesEnum
  path: ../enums/LeafCharacterSizeTypesEnum.md
- rel: allows
  id: enum:HerbaceousLeafPhenologiesEnum
  path: ../enums/HerbaceousLeafPhenologiesEnum.md
- rel: allows
  id: enum:GrowthFrequenciesEnum
  path: ../enums/GrowthFrequenciesEnum.md
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

# LC_Graminoid

Herbaceous Growth Form Element of Graminoid Subtype

LChS reference name `LC_Graminoid` (schema type `LC_GraminoidType`). LCCS3 `xsi:type`: `LC_Graminae`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `cover` | xs:decimal | min, max |  | Cover |
| `heightCM` | xs:decimal | min, max |  | Height |
| `leafCharacterSizeType` | LeafCharacterSizeTypesEnum | `large_leaf`, `medium_leaf`, `small_leaf` |  | Leaf Character Size Type |
| `herbaceousLeafPhenology` | HerbaceousLeafPhenologiesEnum | `NonPerennial`, `Perennial` |  | Herbaceous Leaf Phenology |
| `perennialPercentage` | xs:decimal | min, max |  | Perennial Percentage |
| `nonPerennialGrowthFrequency` | GrowthFrequenciesEnum | `other`, `annual`, `biennial` |  | Non Perennial Growth Frequency |
| `nonPerennialPercentage` | xs:decimal | min, max |  | Non Perennial Percentage |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |
| `lifeFormSpecialization` | LifeFormSpecializationTypesEnum | `bamboos`, `climbers`, `eppphytes`, `stem_succulents`, `tuft_plants`, `arboreal_giant_herbs` |  | Life Form Specialization |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.



# Context: vocab LC_HerbaceousGrowthForm

---
id: element:LC_HerbaceousGrowthForm
kind: vocab_element
title: LC_HerbaceousGrowthForm
lchs_type: LC_HerbaceousGrowthFormType
lccs3_types:
- LC_HerbaceousGrowthForms
properties:
- elementPresenceType
- cover
- heightCM
- leafCharacterSizeType
- herbaceousLeafPhenology
- perennialPercentage
- nonPerennialGrowthFrequency
- nonPerennialPercentage
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
  id: enum:LeafCharacterSizeTypesEnum
  path: ../enums/LeafCharacterSizeTypesEnum.md
- rel: allows
  id: enum:HerbaceousLeafPhenologiesEnum
  path: ../enums/HerbaceousLeafPhenologiesEnum.md
- rel: allows
  id: enum:GrowthFrequenciesEnum
  path: ../enums/GrowthFrequenciesEnum.md
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

# LC_HerbaceousGrowthForm

Growth Form Element of Herbaceous Subtype

LChS reference name `LC_HerbaceousGrowthForm` (schema type `LC_HerbaceousGrowthFormType`). LCCS3 `xsi:type`: `LC_HerbaceousGrowthForms`.

## Properties

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `elementPresenceType` | ElementPresenceTypesEnum | `fixed`, `exclusive`, `conditionalTemporal`, `precluded` | yes | Element Presence Type |
| `cover` | xs:decimal | min, max |  | Cover |
| `heightCM` | xs:decimal | min, max |  | Height |
| `leafCharacterSizeType` | LeafCharacterSizeTypesEnum | `large_leaf`, `medium_leaf`, `small_leaf` |  | Leaf Character Size Type |
| `herbaceousLeafPhenology` | HerbaceousLeafPhenologiesEnum | `NonPerennial`, `Perennial` |  | Herbaceous Leaf Phenology |
| `perennialPercentage` | xs:decimal | min, max |  | Perennial Percentage |
| `nonPerennialGrowthFrequency` | GrowthFrequenciesEnum | `other`, `annual`, `biennial` |  | Non Perennial Growth Frequency |
| `nonPerennialPercentage` | xs:decimal | min, max |  | Non Perennial Percentage |
| `density` | xs:decimal | min, max |  | Density |
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density Area Unit |
| `elementHorizontalSpreading` | ElementHorizontalSpreadingTypeEnum | `clusters`, `regularRowMultipleElement`, `regularRowsMultipleElement`, `regularRowsSingleElement`, `unevenlySpread`, `other` |  | Element Horizontal Spreading |
| `portioning` | xs:decimal | min, max |  | Portioning |
| `temporalType` | SequentialTemporalRelationshipEnum | `sequentialSameYear`, `sequentialOtherYear` |  | Temporal Relationship |
| `lengthOfTemporalRelationship` | xs:decimal | min, max |  | Length of Temporal Relationship |
| `lengthOfTemporalRelationshipUnits` | PeriodUnitsEnum | `second`, `minute`, `hour`, `day`, `week`, `month`, `year` |  | Length of Temporal Relationship Unit |
| `lifeFormSpecialization` | LifeFormSpecializationTypesEnum | `bamboos`, `climbers`, `eppphytes`, `stem_succulents`, `tuft_plants`, `arboreal_giant_herbs` |  | Life Form Specialization |

Ranges are written as two values (min, max). Percentages are 0..100; a full 0..100 range means unspecified.



# Context: vocab LC_Shrub

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
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  
…(truncated)


# Context: vocab LC_Tree

---
id: element:LC_Tree
kind: vocab_element
title: LC_Tree
lchs_type: LC_TreeType
lccs3_types:
- LC_Trees
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

# LC_Tree

Woody Growth Form Element of Tree Subtype

LChS reference name `LC_Tree` (schema type `LC_TreeType`). LCCS3 `xsi:type`: `LC_Trees`.

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
| `uOMArea` | UnitsOfMeasureAreaEnum | `ha`, `m2`, `cm2`, `km2` |  | Density
…(truncated)


# Context: vocab LC_WaterBody

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



# Context: SYSTEM.md

---
id: system:mapbiomas_brazil
kind: system
title: MapBiomas Brazil Collection 10
slug: mapbiomas_brazil
publisher: MapBiomas
version: Collection 10
jurisdiction: Brazil
language: en
n_classes: 38
mode: propose
sources:
- mapbiomas_doc/provenance/legends.json
run_history: []
links:
- rel: has_class
  id: system:mapbiomas_brazil:1
  path: classes/1.md
- rel: has_class
  id: system:mapbiomas_brazil:3
  path: classes/3.md
- rel: has_class
  id: system:mapbiomas_brazil:4
  path: classes/4.md
- rel: has_class
  id: system:mapbiomas_brazil:5
  path: classes/5.md
- rel: has_class
  id: system:mapbiomas_brazil:6
  path: classes/6.md
- rel: has_class
  id: system:mapbiomas_brazil:49
  path: classes/49.md
- rel: has_class
  id: system:mapbiomas_brazil:10
  path: classes/10.md
- rel: has_class
  id: system:mapbiomas_brazil:11
  path: classes/11.md
- rel: has_class
  id: system:mapbiomas_brazil:12
  path: classes/12.md
- rel: has_class
  id: system:mapbiomas_brazil:32
  path: classes/32.md
- rel: has_class
  id: system:mapbiomas_brazil:29
  path: classes/29.md
- rel: has_class
  id: system:mapbiomas_brazil:50
  path: classes/50.md
- rel: has_class
  id: system:mapbiomas_brazil:14
  path: classes/14.md
- rel: has_class
  id: system:mapbiomas_brazil:15
  path: classes/15.md
- rel: has_class
  id: system:mapbiomas_brazil:18
  path: classes/18.md
- rel: has_class
  id: system:mapbiomas_brazil:19
  path: classes/19.md
- rel: has_class
  id: system:mapbiomas_brazil:39
  path: classes/39.md
- rel: has_class
  id: system:mapbiomas_brazil:20
  path: classes/20.md
- rel: has_class
  id: system:mapbiomas_brazil:40
  path: classes/40.md
- rel: has_class
  id: system:mapbiomas_brazil:62
  path: classes/62.md
- rel: has_class
  id: system:mapbiomas_brazil:41
  path: classes/41.md
- rel: has_class
  id: system:mapbiomas_brazil:36
  path: classes/36.md
- rel: has_class
  id: system:mapbiomas_brazil:46
  path: classes/46.md
- rel: has_class
  id: system:mapbiomas_brazil:47
  path: classes/47.md
- rel: has_class
  id: system:mapbiomas_brazil:35
  path: classes/35.md
- rel: has_class
  id: system:mapbiomas_brazil:48
  path: classes/48.md
- rel: has_class
  id: system:mapbiomas_brazil:9
  path: classes/9.md
- rel: has_class
  id: system:mapbiomas_brazil:21
  path: classes/21.md
- rel: has_class
  id: system:mapbiomas_brazil:22
  path: classes/22.md
- rel: has_class
  id: system:mapbiomas_brazil:23
  path: classes/23.md
- rel: has_class
  id: system:mapbiomas_brazil:24
  path: classes/24.md
- rel: has_class
  id: system:mapbiomas_brazil:30
  path: classes/30.md
- rel: has_class
  id: system:mapbiomas_brazil:75
  path: classes/75.md
- rel: has_class
  id: system:mapbiomas_brazil:25
  path: classes/25.md
- rel: has_class
  id: system:mapbiomas_brazil:26
  path: classes/26.md
- rel: has_class
  id: system:mapbiomas_brazil:33
  path: classes/33.md
- rel: has_class
  id: system:mapbiomas_brazil:31
  path: classes/31.md
- rel: has_class
  id: system:mapbiomas_brazil:27
  path: classes/27.md
schema: okf/0.1
---

# MapBiomas Brazil Collection 10

MapBiomas · Collection 10 · Brazil

## Scope statement (verbatim)

_none found_

## Framing summary

_not yet extracted_

## Classes (38)

| code | class | status |
|---|---|---|
| 1 | [Forest](classes/1.md) | titles_only |
| 3 | [Forest Formation](classes/3.md) | titles_only |
| 4 | [Savanna Formation](classes/4.md) | titles_only |
| 5 | [Mangrove](classes/5.md) | titles_only |
| 6 | [Floodable Forest](classes/6.md) | titles_only |
| 49 | [Wooded Sandbank Vegetation](classes/49.md) | titles_only |
| 10 | [Herbaceous and Shrubby Vegetation](classes/10.md) | titles_only |
| 11 | [Wetland](classes/11.md) | titles_only |
| 12 | [Grassland](classes/12.md) | titles_only |
| 32 | [Hypersaline Tidal Flat](classes/32.md) | titles_only |
| 29 | [Rocky Outcrop](classes/29.md) | titles_only |
| 50 | [Herbaceous Sandbank Vegetation](classes/50.md) | titles_only |
| 14 | [Farming](classes/14.md) | titles_only |
| 15 | [Pasture](classes/15.md) | titles_only |
| 18 | [Agriculture](classes/18.md) | titles_only |
| 19 | [Temporary Crop](classes/19.md) | titles_only |
| 39 | [Soybean](classes/39.md) | titles_only |
| 20 | [Sugar cane](classes/20.md) | titles_only |
| 40 | [Rice](classes/40.md) | titles_only |
| 62 | [Cotton (beta)](classes/62.md) | titles_only |
| 41 | [Other Temporary Crops](classes/41.md) | titles_only |
| 36 | [Perennial Crop](classes/36.md) | titles_only |
| 46 | [Coffee](classes/46.md) | titles_only |
| 47 | [Citrus](classes/47.md) | titles_only |
| 35 | [Palm Oil](classes/35.md) | titles_only |
| 48 | [Other Perennial Crops](classes/48.md) | titles_only |
| 9 | [Forest Plantation](classes/9.md) | titles_only |
| 21 | [Mosaic of Uses](classes/21.md) | titles_only |
| 22 | [Non vegetated area](classes/22.md) | titles_only |
| 23 | [Beach, Dune and Sand Spot](classes/23.md) | titles_only |
| 24 | [Urban Area](classes/24.md) | titles_only |
| 30 | [Mining](classes/30.md) | titles_only |
| 75 | [Photovoltaic Power Plant (beta)](classes/75.md) | titles_only |
| 25 | [Other non Vegetated Areas](classes/25.md) | titles_only |
| 26 | [Water](classes/26.md) | titles_only |
| 33 | [River, Lake and Ocean](classes/33.md) | titles_only |
| 31 | [Aquaculture](classes/31.md) | titles_only |
| 27 | [Not Observed](classes/27.md) | titles_only |



# Context: all classes of this system (code | name | parent | status | elements)

- 1 | Forest | parent - | status titles_only | elements -
- 10 | Herbaceous and Shrubby Vegetation | parent - | status titles_only | elements -
- 11 | Wetland | parent - | status titles_only | elements -
- 12 | Grassland | parent - | status titles_only | elements -
- 14 | Farming | parent - | status titles_only | elements -
- 15 | Pasture | parent - | status titles_only | elements -
- 18 | Agriculture | parent - | status titles_only | elements -
- 19 | Temporary Crop | parent - | status titles_only | elements -
- 20 | Sugar cane | parent - | status titles_only | elements -
- 21 | Mosaic of Uses | parent - | status titles_only | elements -
- 22 | Non vegetated area | parent - | status titles_only | elements -
- 23 | Beach, Dune and Sand Spot | parent - | status titles_only | elements -
- 24 | Urban Area | parent - | status titles_only | elements -
- 25 | Other non Vegetated Areas | parent - | status titles_only | elements -
- 26 | Water | parent - | status titles_only | elements -
- 27 | Not Observed | parent - | status titles_only | elements -
- 29 | Rocky Outcrop | parent - | status titles_only | elements -
- 3 | Forest Formation | parent - | status titles_only | elements -
- 30 | Mining | parent - | status titles_only | elements -
- 31 | Aquaculture | parent - | status titles_only | elements -
- 32 | Hypersaline Tidal Flat | parent - | status titles_only | elements -
- 33 | River, Lake and Ocean | parent - | status titles_only | elements -
- 35 | Palm Oil | parent - | status titles_only | elements -
- 36 | Perennial Crop | parent - | status titles_only | elements -
- 39 | Soybean | parent - | status titles_only | elements -
- 4 | Savanna Formation | parent - | status titles_only | elements -
- 40 | Rice | parent - | status titles_only | elements -
- 41 | Other Temporary Crops | parent - | status titles_only | elements -
- 46 | Coffee | parent - | status titles_only | elements -
- 47 | Citrus | parent - | status titles_only | elements -
- 48 | Other Perennial Crops | parent - | status titles_only | elements -
- 49 | Wooded Sandbank Vegetation | parent - | status titles_only | elements -
- 5 | Mangrove | parent - | status titles_only | elements -
- 50 | Herbaceous Sandbank Vegetation | parent - | status titles_only | elements -
- 6 | Floodable Forest | parent - | status titles_only | elements -
- 62 | Cotton (beta) | parent - | status titles_only | elements -
- 75 | Photovoltaic Power Plant (beta) | parent - | status titles_only | elements -
- 9 | Forest Plantation | parent - | status titles_only | elements -


# Context: class 4

---
id: system:mapbiomas_brazil:4
kind: class
title: 4 Savanna Formation
system: system:mapbiomas_brazil
code: '4'
name: Savanna Formation
class_id: '4'
status: titles_only
parent_code: ''
colour: '#7dc975'
definition_language: en
source_span: legends.json:brazil row 3
element_refs: []
confidence: ''
land_use_hint: ''
nearest_examples: []
open_questions: []
links:
- rel: in_system
  id: system:mapbiomas_brazil
  path: ../SYSTEM.md
rows_in: ../elements.csv
schema: okf/0.1
---

# 4 Savanna Formation

## Definition (verbatim)

_titles only: no definition in the source_

## Decomposition

_not yet proposed_



# Context: nearest registry example registry:L45:Sa (score 0.424)

---
id: registry:L45:Sa
kind: class
title: Sa Tree savanna
system: registry:L45
code: Sa
name: Tree savanna
status: registered
decomposed: true
file_class_id: '20'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Tree
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Tree
  path: ../../../vocab/elements/LC_Tree.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Sa Tree savanna

## Definition (verbatim, FAO LCLR)

Lands with herbaceous types of cover. Tree cover between 4–20%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 21 | 22 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 21 | 22 Mandatory | `LC_HerbaceousGrowthForm` |  | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 21 | 25 Mandatory | `LC_Tree` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 21 | 25 Mandatory | `LC_Tree` |  | 4.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `20`.



# Context: nearest registry example registry:L45:Sar (score 0.424)

---
id: registry:L45:Sar
kind: class
title: Sar Shrub savanna
system: registry:L45
code: Sar
name: Shrub savanna
status: registered
decomposed: true
file_class_id: '28'
n_rows: 30
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_Shrub
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_Shrub
  path: ../../../vocab/elements/LC_Shrub.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Sar Shrub savanna

## Definition (verbatim, FAO LCLR)

Lands with herbaceous types of cover. Shrub cover between 4–20%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 29 | 2A Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 29 | 2A Mandatory | `LC_HerbaceousGrowthForm` |  | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 29 | 2D Mandatory | `LC_Shrub` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 29 | 2D Mandatory | `LC_Shrub` |  | 4.0–20.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `28`.



# Context: nearest registry example registry:L45:Sh (score 0.412)

---
id: registry:L45:Sh
kind: class
title: Sh Grass savanna
system: registry:L45
code: Sh
name: Grass savanna
status: registered
decomposed: true
file_class_id: '30'
n_rows: 31
rows_in: ../elements.csv
element_refs:
- LC_HerbaceousGrowthForm
- LC_WoodyGrowthForm
links:
- rel: in_system
  id: registry:L45
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_HerbaceousGrowthForm
  path: ../../../vocab/elements/LC_HerbaceousGrowthForm.md
- rel: uses_type
  id: element:LC_WoodyGrowthForm
  path: ../../../vocab/elements/LC_WoodyGrowthForm.md
sources:
- okf/registry/_raw/L45/L45.lccs
schema: okf/0.1
---

# Sh Grass savanna

## Definition (verbatim, FAO LCLR)

Lands with herbaceous types of cover. Tree and shrub cover is <4%.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 31 | 32 Mandatory | `LC_HerbaceousGrowthForm` | Mandatory |  | height 80.0–300.0 | LC_VegetationArtificialityCharacteristic |
| 31 | 32 Mandatory | `LC_HerbaceousGrowthForm` |  | 40.0–100.0 |  | LC_VegetationArtificialityCharacteristic |
| 31 | 35 Optional | `LC_WoodyGrowthForm` | Mandatory |  |  | LC_VegetationArtificialityCharacteristic |
| 31 | 35 Optional | `LC_WoodyGrowthForm` |  | 1.0–4.0 |  | LC_VegetationArtificialityCharacteristic |

Full rows: `../elements.csv`, class_id `30`.

