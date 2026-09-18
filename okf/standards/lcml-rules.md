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
