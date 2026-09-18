---
id: skill:decompose-class
kind: guide
title: "Skill: decompose-class"
schema: okf/0.1
name: decompose-class
description: Propose the LCML element decomposition of one class, down to the smallest unit, with evidence.
inputs: [system, code]
apply: apply_decompose
manifest: ../../agents/manifests/decompose-class.json
---

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
