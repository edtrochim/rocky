---
id: registry:L25:Cl
kind: class
title: Cl Bowal lateritic crust
system: registry:L25
code: Cl
name: Bowal lateritic crust
status: registered
decomposed: true
file_class_id: 2B1
n_rows: 15
rows_in: ../elements.csv
element_refs:
- LC_Hardpan
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Hardpan
  path: ../../../vocab/elements/LC_Hardpan.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Cl Bowal lateritic crust

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element hard pans with iron pan/laterite type.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2B2 | 2B3 Mandatory | `LC_Hardpan` | Mandatory |  | type=Ironpan/Laterite |  |

Full rows: `../elements.csv`, class_id `2B1`.
