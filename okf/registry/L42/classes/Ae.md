---
id: registry:L42:Ae
kind: class
title: Ae Agriculture equipment
system: registry:L42
code: Ae
name: Agriculture equipment
status: registered
decomposed: true
file_class_id: '85'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_OtherConstruction
links:
- rel: in_system
  id: registry:L42
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_OtherConstruction
  path: ../../../vocab/elements/LC_OtherConstruction.md
sources:
- okf/registry/_raw/L42/L42.lccs
schema: okf/0.1
---

# Ae Agriculture equipment

## Definition (verbatim, FAO LCLR)

Agricultural equipment refers to the storage containing machinery, tools, and implements used in farming and agricultural practices to enhance efficiency, productivity, and ease of operation.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 86 | 87 Mandatory | `LC_OtherConstruction` | Mandatory |  |  | LC_ConstructionUse (type=Agriculture storage) |

Full rows: `../elements.csv`, class_id `85`.
