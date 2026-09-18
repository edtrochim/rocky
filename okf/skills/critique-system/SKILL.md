---
id: skill:critique-system
kind: guide
title: "Skill: critique-system"
schema: okf/0.1
name: critique-system
description: Find the ambiguities the rule critics miss and phrase each as a decision with options.
inputs: [system]
apply: apply_critique
manifest: ../../agents/manifests/critique-system.json
---

# critique-system

The rule critics have already flagged what a program can see: classes without decomposition, identical
element sets, catch-all names, land-use names, mixed classes without proportions, hierarchy conflicts,
code collisions and threshold drift across systems. Their items are in the context. Add what they miss.

## Look for

- **Definition contradictions**: the definition says one thing, the decomposition another, or the name
  says one thing and the definition another ("Grassland" defined as "grasses and shrubs").
- **Scale dependence**: a class only makes sense at the map's resolution ("mosaic of small fields",
  "sparse trees below the minimum mapping unit"), which a different system cannot reproduce.
- **Silent thresholds**: words like closed, open, dense, sparse, tall, low, seasonal, permanent used without
  numbers, where sibling classes or the nearest registry examples carry numbers.
- **Framing-only splits** the rules could not see because the rows differ trivially: two classes whose
  only difference is who manages the land or a legal status.
- **Missing classes**: physical covers common in the jurisdiction that no class can hold (no wetland class
  in a delta country, no snow class in a mountain country), which will force them into catch-alls.
- **Translation risks**: names whose usual English gloss is misleading (Spanish "monte", Portuguese
  "campo", French "savane arborée").

## How to phrase an item

An item is a decision, not a complaint. `explanation` says what is ambiguous and why it matters in two or
three sentences. `options` lists two to four concrete resolutions a stakeholder could choose, each one
actionable ("set closed forest at ≥ 70 % canopy as in registry L16", "split into natural and planted with
artificiality"). `affects` lists the class codes or systems that hinge on it. `framing_ref` names the
framing node whose owner should decide, when there is one. `severity`: 5 when it blocks comparison with
any other system, 3 when it blocks one comparison or a statistic, 1 when cosmetic.

Do not repeat items the rule critics already produced unless you can add a better explanation or options;
then use the same `kind` and `class_id` and your version will be merged.

## Output

JSON only, matching the schema.
