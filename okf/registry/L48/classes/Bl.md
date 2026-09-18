---
id: registry:L48:Bl
kind: class
title: Bl Bare land (current fallow)
system: registry:L48
code: Bl
name: Bare land (current fallow)
status: registered
decomposed: true
file_class_id: 1D
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L48
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L48/L48.lccs
schema: okf/0.1
---

# Bl Bare land (current fallow)

## Definition (verbatim, FAO LCLR)

Land cover which consists of bare soils either natural or cropland that through fallow period (cultivation absence).

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 1E | 1F Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `1D`.
