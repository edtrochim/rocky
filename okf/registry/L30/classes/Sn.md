---
id: registry:L30:Sn
kind: class
title: Sn Bare ground
system: registry:L30
code: Sn
name: Bare ground
status: registered
decomposed: true
file_class_id: 10C
n_rows: 22
rows_in: ../elements.csv
element_refs:
- LC_BareRock
- LC_BareSoil
- LC_CoarseMineralFragments
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
- rel: uses_type
  id: element:LC_BareSoil
  path: ../../../vocab/elements/LC_BareSoil.md
- rel: uses_type
  id: element:LC_CoarseMineralFragments
  path: ../../../vocab/elements/LC_CoarseMineralFragments.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Sn Bare ground

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 10D | 10E Mandatory | `LC_BareRock` | Exclusive |  |  |  |
| 10D | 10E Mandatory | `LC_CoarseMineralFragments` | Exclusive |  |  |  |
| 10D | 10E Mandatory | `LC_BareSoil` | Exclusive |  |  |  |

Full rows: `../elements.csv`, class_id `10C`.
