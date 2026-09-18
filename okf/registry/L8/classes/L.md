---
id: registry:L8:L
kind: class
title: L Standing artificial water body - lake
system: registry:L8
code: L
name: Standing artificial water body - lake
status: registered
decomposed: true
file_class_id: FF
n_rows: 29
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

# L Standing artificial water body - lake

## Definition (verbatim, FAO LCLR)

Artificial/Natural standing water reservoir that is bigger than a pond. It is an area of variable size filled with water, localized in a basin, that is surrounded by land, apart from any river or other outlet that serves to feed or drain the lake.

## Decomposition (from the registry file)

| pattern | stratum | element | presence | cover | other properties | characteristics |
|---|---|---|---|---|---|---|
| 100 | 101 Mandatory | `LC_WaterBody` | Mandatory |  | dynamics=Standing; position=Above Surface | LC_ArtificialityCharacteristic (type=Artificial); LC_UserDefinedElementCharacteristic (userid=uds_0ad57fa0-ebff-11e5-8e21-780cb82883be, LC_Property[LC_PropertyString@size_ha]/value=> 50); LC_WaterSalinityCharacteristic (type=Fresh) |

Full rows: `../elements.csv`, class_id `FF`.
