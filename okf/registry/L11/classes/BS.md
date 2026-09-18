---
id: registry:L11:BS
kind: class
title: BS Bare soil
system: registry:L11
code: BS
name: Bare soil
status: registered
decomposed: true
file_class_id: DB
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareSoil
links:
- rel: in_system
  id: registry:L11
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
sources:
- okf/registry/_raw/L11/L11.lccs
schema: okf/0.1
---

# BS Bare soil

## Definition (verbatim, FAO LCLR)

Bare area/undifferentiated area not used for cultivation and usually devoid of grass and shrub cover / Rock outcrops.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| DC | DD Mandatory | `LC_BareSoil` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `DB`.
