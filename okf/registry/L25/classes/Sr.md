---
id: registry:L25:Sr
kind: class
title: Sr Bare rocks
system: registry:L25
code: Sr
name: Bare rocks
status: registered
decomposed: true
file_class_id: 2AD
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_BareRock
links:
- rel: in_system
  id: registry:L25
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_BareRock
  path: ../../../vocab/elements/LC_BareRock.md
sources:
- okf/registry/_raw/L25/L25.lccs
schema: okf/0.1
---

# Sr Bare rocks

## Definition (verbatim, FAO LCLR)

This class is very basic, and generic being constituted by one mandatory stratum that defines the overall class structure. The strata are constituted by one basic element rock.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 2AE | 2AF Mandatory | `LC_BareRock` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `2AD`.
