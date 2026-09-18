---
id: skill:extract-framing
kind: guide
title: "Skill: extract-framing"
schema: okf/0.1
name: extract-framing
description: Find the institutions, instruments and purposes that shape the class names and thresholds of a system.
inputs: [system]
apply: apply_framing
manifest: ../../agents/manifests/extract-framing.json
---

# extract-framing

Class names are outputs of regulation, mandate and history, not only of vegetation. This skill records
that framing as nodes so that a later comparison can tell a translation problem (same physical cover,
different words) from a real collision, and so that a decision about a class is routed to whoever owns
the rule behind it.

## What counts as an instrument

- A law or regulation that defines a term the system uses (a forest law's canopy threshold, a wetland
  convention's definition, a native-forest subsidy scheme that separates primary from secondary forest).
- A policy or programme the map serves (deforestation monitoring, agricultural statistics, carbon
  accounting, land tenure, urban planning).
- A reporting obligation (UNFCCC land categories, SDG indicators, FAO Forest Resources Assessment).
- A scientific convention the system inherits (a phytogeographic biome scheme, a vegetation typology).
- A mapping practice that fixed a threshold (minimum mapping unit, sensor resolution, "not observed"
  classes for cloud cover).

## How to work

1. Read the system's scope statement, the notes, and the source blocks for prefaces, legal references,
   citations and acknowledgements. Read the class nodes for names that carry a jurisdiction's vocabulary
   (Cerrado, Caatinga, Bosque nativo, Steppe, Andean, Restinga, Mosaic of uses).
2. For each instrument you can evidence, produce one entry with a verbatim quote or a precise reference and
   the class codes it shapes. Say concretely what it does: sets a threshold, forces a split, gives the name,
   defines the aggregate level.
3. Classes with no framing evidence go in `none_stated_for`. Do not invent instruments; if you suspect one
   (a class named after a biome that is legally defined in that country) say so in `effect_on_classes`
   with "likely" and instrument_type `other`, and keep the evidence honest.
4. `summary`: who made the system, for what purpose, under which rules, in five sentences at most.

## Output

JSON only, matching the schema.
