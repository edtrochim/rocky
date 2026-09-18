---
id: registry:L30:Dse
kind: class
title: Dse Landfull and extraction site
system: registry:L30
code: Dse
name: Landfull and extraction site
status: registered
decomposed: true
file_class_id: '129'
n_rows: 18
rows_in: ../elements.csv
element_refs:
- LC_DumpSite
- LC_Extraction
links:
- rel: in_system
  id: registry:L30
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_DumpSite
  path: ../../../vocab/elements/LC_DumpSite.md
- rel: uses_type
  id: element:LC_Extraction
  path: ../../../vocab/elements/LC_Extraction.md
sources:
- okf/registry/_raw/L30/L30.lccs
schema: okf/0.1
---

# Dse Landfull and extraction site

## Definition (verbatim, FAO LCLR)

_none given_

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 12A | 12B Mandatory | `LC_Extraction` | Exclusive |  |  |  |
| 12A | 12B Mandatory | `LC_DumpSite` | Exclusive |  |  |  |

Full rows: `../elements.csv`, class_id `129`.
