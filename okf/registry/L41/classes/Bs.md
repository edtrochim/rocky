---
id: registry:L41:Bs
kind: class
title: Bs Bare soil
system: registry:L41
code: Bs
name: Bare soil
status: registered
decomposed: true
file_class_id: 9E
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_BareSoil
links:
- rel: in_system
  id: registry:L41
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L41/L41.lccs
schema: okf/0.1
---

# Bs Bare soil

## Definition (verbatim, FAO LCLR)

Exposed soil areas with no vegetation (<4%), often due to erosion or overuse of agricultural lands. Exposed rock surfaces with minimal or no vegetation (<4%), commonly found in highlands or karst landscapes.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 9F | 147 Optional | `LC_BareRock` | Mandatory |  |  |  |
| 9F | A0 Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `9E`.
