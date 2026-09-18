---
id: registry:L8:Po
kind: class
title: Po Ponds
system: registry:L8
code: Po
name: Ponds
status: registered
decomposed: true
file_class_id: '104'
n_rows: 25
rows_in: ../elements.csv
element_refs:
- LC_WaterBody
links:
- rel: in_system
  id: registry:L8
  path: ../SYSTEM.md
- rel: uses_type
  id: element:LC_WaterBody
  path: ../../../vocab/elements/LC_WaterBody.md
sources:
- okf/registry/_raw/L8/L8.lccs
schema: okf/0.1
---

# Po Ponds

## Definition (verbatim, FAO LCLR)

pond is a human-constructed body of standing water with an area of variable size that is usually smaller than a lake.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 105 | 106 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing; position=Above Surface | LC_ArtificialityCharacteristic (type=Artificial); LC_UserDefinedElementCharacteristic (userid=uds_0ad57fa0-ebff-11e5-8e21-780cb82883be, LC_Property[LC_PropertyString@size_ha]/value=> 0.3) |

Full rows: `../elements.csv`, class_id `104`.
