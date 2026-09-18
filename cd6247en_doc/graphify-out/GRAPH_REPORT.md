# Graph Report - cd6247en_doc  (2026-09-17)

## Corpus Check
- Corpus is ~48,182 words - fits in a single context window. You may not need a graph.

## Summary
- 468 nodes · 851 edges · 20 communities
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 83 edges (avg confidence: 0.85)
- Token cost: 424,000 input · 62,715 output

## Community Hubs (Navigation)
- Abiotic & Artificial Surface Elements
- Strata, Patterns & Horizontal Disposition
- Backward Compatibility & Registration
- Vegetation Science References & Leaf Types
- Class Characteristics & Crop Attributes
- Annex C Worked Examples
- Water, Ice & Snow Characteristics
- Metalanguage Elements & Glossary
- Value Objects & Permitted Values
- Leaf Phenology & Growth Frequency
- Soil, Sand & Surface Arrangement
- Bare Soil, Rock & Deposits
- Conformance & General Feature Model
- Application Schema & Classification Systems
- LCCS Lineage & Bibliography
- FAO / ISO TC 211 Governance
- Water Body Concepts
- ISO 19144-1 Legend & Feature Catalogue
- Floristic & Species Characteristics
- Coverage Geometry

## God Nodes (most connected - your core abstractions)
1. `Extension through registration` - 34 edges
2. `LC_Element` - 33 edges
3. `Land Cover Meta Language (LCML)` - 29 edges
4. `ISO 19144-2:2023 Land Cover Meta Language (LCML), Edition 2` - 23 edges
5. `LC_GrowthFormCharacteristic` - 23 edges
6. `LC_PermittedPercentageRange` - 22 edges
7. `ISO/TS 19144-3 Land Use Meta Language (LUML)` - 21 edges
8. `LC_Stratum` - 20 edges
9. `LC_LandCoverClass` - 18 edges
10. `ISO 19144-2:2023 Land Cover Meta Language (LCML)` - 18 edges

## Surprising Connections (you probably didn't know these)
- `LC_GrowthFormCharacteristic` --implements--> `LC_ClassCharacteristic`  [AMBIGUOUS]
  cd6247en.pdf → cd6247en.pdf  _Bridges community 4 → community 0_
- `Land Cover Meta Language (LCML)` --semantically_similar_to--> `Arnold et al. 2016 The EAGLE Concept`  [INFERRED] [semantically similar]
  cd6247en.pdf → cd6247en.pdf  _Bridges community 8 → community 1_
- `Land Cover Meta Language (LCML)` --conceptually_related_to--> `UN FAO / Southampton / STIIMA-CNR 2022 Land Characterization Meta-Language`  [INFERRED]
  cd6247en.pdf → cd6247en.pdf  _Bridges community 8 → community 14_
- `Macropattern (soil / sand)` --semantically_similar_to--> `Horizontal pattern`  [INFERRED] [semantically similar]
  cd6247en.pdf → cd6247en.pdf  _Bridges community 1 → community 11_
- `Conformance class 2: Comparison of Land Cover classification systems` --conceptually_related_to--> `Pure (single concept) element principle`  [INFERRED]
  cd6247en.pdf → cd6247en.pdf  _Bridges community 8 → community 12_

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Three semantic levels: metalanguage > classification system > legend** — cd6247en_lc_landcoverclassificationsystemmetalanguage, cd6247en_lc_landcoverclassificationsystem, cd6247en_lc_landcoverclassdescriptor, cd6247en_lc_landcoverclass, cd6247en_cl_legendclass [EXTRACTED 1.00]
- **Subtypes of LC_GrowthForm** — cd6247en_lc_woodygrowthform, cd6247en_lc_herbaceousgrowthform, cd6247en_lc_lichenandmoss, cd6247en_lc_algae, cd6247en_lc_growthform [EXTRACTED 1.00]
- **Code lists supporting the LCML object structure (Figure 4)** — cd6247en_lc_elementhorizontalspreadingtype, cd6247en_lc_elementpresencetype, cd6247en_lc_stratumpresencetype, cd6247en_lc_sequentialtemporalrelationshiptype, cd6247en_lc_ontoptype [EXTRACTED 1.00]
- **Subtypes of LC_AbioticElement** — cd6247en_lc_abioticelement, cd6247en_lc_artificialsurfaceelement, cd6247en_lc_naturalsurfaceelement, cd6247en_lc_waterbodyandassociatedsurfaceelement [EXTRACTED 1.00]
- **The 11 subtypes of LC_GrowthFormCharacteristic** — cd6247en_lc_growthformcharacteristic, cd6247en_lc_floristicaspectscharacteristic, cd6247en_lc_allometricmeasurementscharacteristic, cd6247en_lc_growthformagecharacteristic, cd6247en_lc_burntstatuscharacteristic, cd6247en_lc_deadstatuscharacteristic, cd6247en_lc_waterstresscharacteristic, cd6247en_lc_vegetationdamagecharacteristic, cd6247en_lc_growthformillnesscharacteristic, cd6247en_lc_grazedcharacteristic, cd6247en_lc_mowedcharacteristic, cd6247en_lc_vegetationartificialitycharacteristic [EXTRACTED 1.00]
- **The 7 subtypes of LC_CultivatedAndManagedVegetationCharacteristic** — cd6247en_lc_cultivatedandmanagedvegetationcharacteristic, cd6247en_lc_cropyieldcharacteristic, cd6247en_lc_plantationcharacteristic, cd6247en_lc_cropgrowingparametercharacteristic, cd6247en_lc_watersupplyperiodcharacteristic, cd6247en_lc_fieldsizecharacteristic, cd6247en_lc_mechanicalerosioncontrolfeaturecharacteristic, cd6247en_lc_ploughedcharacteristic [EXTRACTED 1.00]
- **LCML extension and registration regime** — cd6247en_extension_process, cd6247en_registration, cd6247en_backward_compatibility, cd6247en_metalanguage_extension_register, cd6247en_iso_19144_4, cd6247en_iso_19135_1, cd6247en_requirement_3, cd6247en_requirement_4 [EXTRACTED 1.00]
- **LC_ValueObject permitted numeric type hierarchy instantiated to ISO 19103 basic types** — cd6247en_lc_valueobject, cd6247en_lc_permittedrealvaluetype, cd6247en_lc_permittedintegervaluetype, cd6247en_lc_permittedpercentagevaluetype, cd6247en_lc_permittedrealrange, cd6247en_lc_permittedposrealrange, cd6247en_lc_permittedposintegerrange, cd6247en_lc_permittedpercentagerange, cd6247en_number, cd6247en_unitofmeasure, cd6247en_iso_19103 [EXTRACTED 1.00]
- **Four levels of abstraction: LCML, classification system, Application Schema, data set** — cd6247en_lcml, cd6247en_classification_system, cd6247en_legend, cd6247en_application_schema, cd6247en_feature_catalogue, cd6247en_general_feature_model, cd6247en_levels_of_abstraction [EXTRACTED 1.00]
- **Interrelated LCML items: cover, portioning, strata, horizontal pattern** — cd6247en_cover, cd6247en_element_portioning, cd6247en_strata_portioning, cd6247en_stratum, cd6247en_horizontal_pattern [EXTRACTED 1.00]
- **Land Use classes moved from ISO 19144-2:2012 to ISO/TS 19144-3** — cd6247en_lc_treeareamanagementpractices, cd6247en_lc_grazing, cd6247en_lc_mowing, cd6247en_lc_pestcontrol, cd6247en_lc_cropfertilization, cd6247en_lc_ploughing, cd6247en_iso_19144_3 [EXTRACTED 1.00]
- **New characteristics describing physiognomic effects of land use activities** — cd6247en_lc_grazedcharacteristic, cd6247en_lc_mowedcharacteristic, cd6247en_lc_ploughedcharacteristic, cd6247en_backward_compatibility [EXTRACTED 1.00]

## Communities (20 total, 0 thin omitted)

### Community 0 - "Abiotic & Artificial Surface Elements"
Cohesion: 0.05
Nodes (52): UNFCCC 1992, Characteristic (classification), Climate (class characteristic), ISO 19144-4 Registration and implementation for LC/LU classification, Package LC_Abiotic, LC_AbioticElement, LC_ArtificialSurfaceCategoryCharacteristic, LC_ArtificialSurfaceCharacteristic (+44 more)

### Community 1 - "Strata, Patterns & Horizontal Disposition"
Cohesion: 0.07
Nodes (48): Area of incidence, Area of pertinence, attribute cover, attribute elementPortioning, attribute patternCoverPercentage, attribute patternOccurrence, attribute patternType, attribute presenceType (+40 more)

### Community 2 - "Backward Compatibility & Registration"
Cohesion: 0.07
Nodes (48): Artificial surfaces and associated areas, Backward compatibility through registration, Built-up surface, Clause 9 Extension of LCML, Construction status, Crop yield, Cultivated and managed vegetation, Deprecated registered item (+40 more)

### Community 3 - "Vegetation Science References & Leaf Types"
Cohesion: 0.06
Nodes (39): Algae, Allometric measurements (DBH, crown diameter), Cowardin et al. 1979 Classification of Wetlands, Eiten 1968 Vegetation Forms, Ford-Robertson 1971 Terminology of Forest Science, IPCC 2003 Good Practice Guidance for LULUCF, HELM Harmonised European Land Monitoring 2014, Kuechler & Zonneveld 1988 Handbook of Vegetation Science (+31 more)

### Community 4 - "Class Characteristics & Crop Attributes"
Cohesion: 0.08
Nodes (37): attribute height, attribute lengthOfTemporalRelationship, Intercropping, LC_AllometricMeasurementsCharacteristic, LC_ArtificialDamageType, LC_ArtificialSurfaceDamageCharacteristic, LC_BurntStatusCharacteristic, LC_CropGrowingParameterCharacteristic (+29 more)

### Community 5 - "Annex C Worked Examples"
Cohesion: 0.11
Nodes (37): CORINE Land Cover (EU), Example C.15 Evergreen forest land (Anderson/USGS), Example C.10 Bare field planted with wheat same year (temporal), Example C.8 Boreal and hemi-boreal forest (four strata), Example C.5 Boulders with moss in a grassland (onTop), Example C.7 Building with roof garden (complex onTop), Example C.13 CORINE class 111 Continuous urban areas, Example C.14 CORINE class 244 Agro-forestry areas (+29 more)

### Community 6 - "Water, Ice & Snow Characteristics"
Cohesion: 0.10
Nodes (28): LC_ArtificialityCharacteristic, LC_ArtificialityType, LC_FloatingIce, LC_FloatingIceType, LC_Ice, LC_IceCategoryCharacteristic, LC_IceType (empty code list, populated by registration), LC_NaturalOrSeminaturalVegetationCharacteristic (+20 more)

### Community 7 - "Metalanguage Elements & Glossary"
Cohesion: 0.09
Nodes (26): attribute status (LC_Algae), attribute elementHorizontalSpreading, attribute lifeFormSpecialization, attribute onTop, attribute temporalType, Basic metalanguage-element, density attribute (new, LC_Element), elementSpreadingGeometry attribute (+18 more)

### Community 8 - "Value Objects & Permitted Values"
Cohesion: 0.11
Nodes (24): Antonio Di Gregorio, Metalanguage attributes as templates, Class (classification), Class (UML), Extension process of the LCML, ISO 19103 Conceptual schema language, LC_PermittedIntegerValueType (abstract; Integer; uom attribute), LC_PermittedPercentageValue ({ baseValue >= 0.0, maxValue <= 100.0 }) (+16 more)

### Community 9 - "Leaf Phenology & Growth Frequency"
Cohesion: 0.10
Nodes (22): Annex D (thresholds and detailed code list values), LC_Annual, LC_Aphyllous, LC_Biennal (merged), LC_Biennial, LC_BroadLeaf, LC_BroadLeafShape, LC_BroadLeafVenation (+14 more)

### Community 10 - "Soil, Sand & Surface Arrangement"
Cohesion: 0.12
Nodes (18): attribute density / densityUnitOfMeasure, LC_BareSoil, LC_CoarseMineralFragments, LC_CoarseMineralFragmentType, LC_Dune, LC_DuneType, LC_ElementHorizontalArrangement, LC_LooseAndShiftingSand (+10 more)

### Community 11 - "Bare Soil, Rock & Deposits"
Cohesion: 0.13
Nodes (16): Abiotic natural surface, Bare rock, Bare soil, UNESCO 1973 International Classification and Mapping of Vegetation, Coarse fragments (gravel, stones, boulders), Hardpans (ironpan, petrocalcic, petrogypsic), Inorganic deposits (salt, soda, lime, gypsum), LC_Deposits (+8 more)

### Community 12 - "Conformance & General Feature Model"
Cohesion: 0.18
Nodes (14): Abstract test suite (ATS, Annex A), Africover, ISO 19105:2022 Conformance and testing, C Douglas O'Brien, Conformance class 1: Description of a Land Cover classification system, Conformance class 2: Comparison of Land Cover classification systems, Feature (GFM feature type), General Feature Model (ISO 19109) (+6 more)

### Community 13 - "Application Schema & Classification Systems"
Cohesion: 0.18
Nodes (13): Anderson (USGS) classification, Application Schema, Land Cover classification system, ISO 19118 Encoding, ISO 19123 series Coverage geometry and functions, ISO/TS 19139-1 XML schema implementation, Levels of abstraction (metalanguage, classification system, application schema, data), Land Parcel Identification System (LPIS) of Portugal (+5 more)

### Community 14 - "LCCS Lineage & Bibliography"
Cohesion: 0.22
Nodes (11): Di Gregorio & Jansen 1997 Africover Land Cover Classification, Anderson et al. 1976 USGS land use/land cover classification, CORINE Land Cover (CEC 1993; CLC nomenclature 2017), ISO 19101-1 Reference model Part 1, UN FAO 2000 LCCS v1 user manual, UN FAO 2005 LCCS v2 (Di Gregorio), UN FAO / Southampton / STIIMA-CNR 2022 Land Characterization Meta-Language, SIOSE Spain land occupation information system (+3 more)

### Community 15 - "FAO / ISO TC 211 Governance"
Cohesion: 0.25
Nodes (8): Food and Agriculture Organization of the United Nations (FAO), Fatima Mushtaq, International Organization for Standardization (ISO), ISO/TC 211 Geographic information/Geomatics, ISO/TC 211 Advisory Group 13 on land cover and land use, Lifeng Li, Matieu Henry, Sandra Branteback

### Community 16 - "Water Body Concepts"
Cohesion: 0.29
Nodes (7): Artificiality (natural / artificial water body), Ice (terrestrial / floating), Permafrost, Salinity (TDS), Snow, Water body and associated surface, Water nutrient level

### Community 17 - "ISO 19144-1 Legend & Feature Catalogue"
Cohesion: 0.33
Nodes (7): CL_LegendClass (ISO 19144-1), Feature catalogue (ISO 19110), ISO 19110 Methodology for feature cataloguing, ISO 19144-1 Classification system structure, LC_ / EL_ / LM_ prefix convention, Legend (nomenclature), Register of Legend classes (ISO 19144-1)

### Community 18 - "Floristic & Species Characteristics"
Cohesion: 0.29
Nodes (7): LC_FloristicAspectsCharacteristic, LC_GroupOfPlantSpeciesCharacteristic, LC_GroupOfPlantSpeciesType, LC_NameAttributionCriteriaCharacteristic, LC_SinglePlantSpeciesCharacteristic, LC_SinglePlantSpeciesType, LC_SpeciesName

### Community 19 - "Coverage Geometry"
Cohesion: 0.47
Nodes (6): Discrete coverage, Grid, ISO 19123-1 Schema for coverage geometry and functions, ISO/TS 19130-2:2014 Imagery sensor models, Point cloud, Triangulated irregular network (TIN)

## Ambiguous Edges - Review These
- `LC_GrowthFormCharacteristic` → `LC_ClassCharacteristic`  [AMBIGUOUS]
  cd6247en.pdf · relation: implements
- `LC_HerbaceousLeafPhenology` → `LC_Annual`  [AMBIGUOUS]
  cd6247en.pdf · relation: implements
- `LC_HerbaceousLeafPhenology` → `LC_Biennial`  [AMBIGUOUS]
  cd6247en.pdf · relation: implements

## Knowledge Gaps
- **115 isolated node(s):** `ISO/IEC Directives Part 2 (2018)`, `C Douglas O'Brien`, `Matieu Henry`, `Fatima Mushtaq`, `John Latham` (+110 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 116 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `LC_GrowthFormCharacteristic` and `LC_ClassCharacteristic`?**
  _Edge tagged AMBIGUOUS (relation: implements) - confidence is low._
- **What is the exact relationship between `LC_HerbaceousLeafPhenology` and `LC_Annual`?**
  _Edge tagged AMBIGUOUS (relation: implements) - confidence is low._
- **What is the exact relationship between `LC_HerbaceousLeafPhenology` and `LC_Biennial`?**
  _Edge tagged AMBIGUOUS (relation: implements) - confidence is low._
- **Why does `LC_Element` connect `Metalanguage Elements & Glossary` to `Abiotic & Artificial Surface Elements`, `Strata, Patterns & Horizontal Disposition`, `Backward Compatibility & Registration`, `Vegetation Science References & Leaf Types`, `Class Characteristics & Crop Attributes`, `Annex C Worked Examples`, `Value Objects & Permitted Values`, `Soil, Sand & Surface Arrangement`?**
  _High betweenness centrality (0.243) - this node is a cross-community bridge._
- **Why does `Extension through registration` connect `Abiotic & Artificial Surface Elements` to `Strata, Patterns & Horizontal Disposition`, `Backward Compatibility & Registration`, `Vegetation Science References & Leaf Types`, `Class Characteristics & Crop Attributes`, `Water, Ice & Snow Characteristics`, `Metalanguage Elements & Glossary`, `Value Objects & Permitted Values`, `Soil, Sand & Surface Arrangement`, `Floristic & Species Characteristics`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Why does `Land Cover Meta Language (LCML)` connect `Value Objects & Permitted Values` to `Abiotic & Artificial Surface Elements`, `Strata, Patterns & Horizontal Disposition`, `Metalanguage Elements & Glossary`, `Conformance & General Feature Model`, `Application Schema & Classification Systems`, `LCCS Lineage & Bibliography`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `LC_Element` (e.g. with `Growth form` and `LC_Building`) actually correct?**
  _`LC_Element` has 10 INFERRED edges - model-reasoned connections that need verification._