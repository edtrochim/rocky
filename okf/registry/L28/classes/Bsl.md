---
id: registry:L28:Bsl
kind: class
title: Bsl Open land bare soil
system: registry:L28
code: Bsl
name: Open land bare soil
status: registered
decomposed: true
file_class_id: '88'
n_rows: 17
rows_in: ../elements.csv
element_refs:
- LC_NaturalSurfaceElement
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_NaturalSurfaceElement
  path: ../../../vocab/elements/LC_NaturalSurfaceElement.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Bsl Open land bare soil

## Definition (verbatim, FAO LCLR)

Natural bare surface around larger lakes and disturbed areas.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 8A | 8B Mandatory | `LC_NaturalSurfaceElement` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `88`.
