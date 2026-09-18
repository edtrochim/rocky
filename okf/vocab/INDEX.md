---
id: vocab
kind: guide
title: LCML vocabulary
counts:
  elements: 41
  characteristics: 23
  records: 9
  enums: 56
sources:
- lchs.xsd
- lccs3.xsd
links:
- rel: see
  id: vocab-elements
  path: elements/INDEX.md
- rel: see
  id: vocab-characteristics
  path: characteristics/INDEX.md
schema: okf/0.1
---

# LCML vocabulary

Generated from FAO's LChS schema (ISO 19144-2:2023) with LCCS3 names cross-walked. Do not edit by hand; rerun `okf/tools/build_vocab.py`.

A class is one or more **horizontal patterns**, each a stack of **strata**, each holding **elements**, each element carrying properties and optional **characteristics**.

- [Elements](elements/INDEX.md): 41 types
- [Characteristics](characteristics/INDEX.md): 23 types
- Records: the flat LChS file records, [LC_LegendType](records/LC_LegendType.md), [ObjectsContainerType](records/ObjectsContainerType.md), [LC_ClassType](records/LC_ClassType.md), [LC_ClassCharacteristicsType](records/LC_ClassCharacteristicsType.md), [LC_HorizontalPatternsType](records/LC_HorizontalPatternsType.md), [LC_StrataType](records/LC_StrataType.md), [LC_PropertiesType](records/LC_PropertiesType.md), [LC_CharacteristicsType](records/LC_CharacteristicsType.md), [LC_ElementsType](records/LC_ElementsType.md)
- Enumerations: 56 under `enums/`, one per file, linked from the type that uses them
- `lchs_schema.json`, `lccs3_schema.json`: the same vocabulary for tools
