---
id: registry:L8:DS
kind: class
title: DS Dump sites/ extraction sites
system: registry:L8
code: DS
name: Dump sites/ extraction sites
status: registered
decomposed: true
file_class_id: E7
n_rows: 20
rows_in: ../elements.csv
element_refs:
- LC_DumpSite
- LC_Extraction
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_DumpSite
  path: ../../../vocab/elements/LC_DumpSite.md
- rel: uses_type
  id: element:LC_Extraction
  path: ../../../vocab/elements/LC_Extraction.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# DS Dump sites/ extraction sites

## Definition (verbatim, FAO LCLR)

Extraction site is defined by the absence of the original natural (semi-natural) cover or water surface and land cover, rock or earthy materials are removed by human activity or machinery.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| E8 | E9 Mandatory | `LC_DumpSite` | Exclusive |  | type=Waste Dumps |  |
| E8 | E9 Mandatory | `LC_Extraction` | Exclusive |  | type=Stone or Coal Mining |  |

Full rows: `../elements.csv`, class_id `E7`.
