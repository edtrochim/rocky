---
id: registry:L28:Ice
kind: class
title: Ice Open land ice cap / snow
system: registry:L28
code: Ice
name: Open land ice cap / snow
status: registered
decomposed: true
file_class_id: '96'
n_rows: 14
rows_in: ../elements.csv
element_refs:
- LC_Snow
links:
- rel: in_system
  id: registry:L28
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_Snow
  path: ../../../vocab/elements/LC_Snow.md
sources:
- okf/registry/_raw/L28/L28.lccs
schema: okf/0.1
---

# Ice Open land ice cap / snow

## Definition (verbatim, FAO LCLR)

Area cover with snow/ice cap.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 97 | 98 Mandatory | `LC_Snow` | Mandatory |  |  |  |

Full rows: `../elements.csv`, class_id `96`.
