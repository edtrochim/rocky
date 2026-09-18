# Graph Report - cd6231en_doc  (2026-09-17)

## Corpus Check
- Corpus is ~22,607 words - fits in a single context window. You may not need a graph.

## Summary
- 307 nodes · 577 edges · 13 communities
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 53 edges (avg confidence: 0.81)
- Token cost: 180,000 input · 31,259 output

## Community Hubs (Navigation)
- Agroforestry Examples & LCML Characteristics
- Registration, Extension & Farming Activities
- Conformance & Classification System Comparison
- Land Use Functions & Conservation/Heritage
- Activity Arrangement & Functional Relationships
- ISO 19144 Series & Governance
- Metamodel Descriptors & Test Suite
- Transport, Logistics & Services
- Heavy Production Industry
- Natural Products Harvesting
- Buffering & Shielding Activities
- Energy Production
- Other / Non-distinct Use

## God Nodes (most connected - your core abstractions)
1. `Registration of code lists, characteristics and classification systems` - 46 edges
2. `Land Use Meta Language (LUML)` - 38 edges
3. `ISO/TS 19144-3:2024 Land Use Meta Language (LUML)` - 28 edges
4. `LU_PrimaryProductionActivities (abstract)` - 24 edges
5. `LU_Activities` - 23 edges
6. `ISO 19144-2 Land Cover Meta Language (LCML)` - 22 edges
7. `Land Cover Land Use functional link` - 16 edges
8. `Example 1: Pure Land Cover description of agroforestry parkland` - 15 edges
9. `LU_FunctionsElementArrangement (LU_FunctionalElementArrangement)` - 13 edges
10. `Example 2: Land Cover description augmented with Land Use information` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Land Use Meta Language (LUML)` --implements--> `UML 2.5.1 Unified Modelling Language`  [INFERRED]
  cd6231en.pdf → cd6231en.pdf  _Bridges community 6 → community 2_
- `Land Use Meta Language (LUML)` --conceptually_related_to--> `Three semantic levels: legend, classification system, metalanguage`  [INFERRED]
  cd6231en.pdf → cd6231en.pdf  _Bridges community 2 → community 5_
- `LU_FunctionalElementArrangement` --implements--> `Land Use function`  [INFERRED]
  cd6231en.pdf → cd6231en.pdf  _Bridges community 3 → community 0_
- `Land Events` --conceptually_related_to--> `Land Use activity`  [INFERRED]
  cd6231en.pdf → cd6231en.pdf  _Bridges community 4 → community 3_
- `LU_LandUseClassStructure package` --references--> `LU_LandUseClass`  [INFERRED]
  cd6231en.pdf → cd6231en.pdf  _Bridges community 4 → community 5_

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **High level structure of the Land Use Classification Model (Figure 2)** — cd6231en_lu_landuseclassificationsystemmetalanguage, cd6231en_lu_landuseclassdescriptor, cd6231en_lu_landuseclassificationsystem, cd6231en_lu_landuseclass, cd6231en_cl_legendclass [EXTRACTED 1.00]
- **Combined Land Cover Land Use structure, Description Type 3 (Figure 5)** — cd6231en_lu_landcharacterizationmetalanguage, cd6231en_lu_landcharacterizationdescriptor, cd6231en_lu_landcoverlanduserelationship, cd6231en_lu_functionselementarrangement, cd6231en_lc_horizontalpattern, cd6231en_lc_classcharacteristics, cd6231en_lu_relationshiptype, cd6231en_lu_temporalrelationshiptype [EXTRACTED 1.00]
- **Functions element arrangement (Figure 6)** — cd6231en_lu_landuseclassdescriptor, cd6231en_lu_functionselementarrangement, cd6231en_lu_landusefunctionelement, cd6231en_lu_activitiesarrangement, cd6231en_lu_activities [EXTRACTED 1.00]
- **Four relationship types forming the activity arrangement structure** — cd6231en_activity_arrangement_structure, cd6231en_functional_relationship, cd6231en_temporal_relationship, cd6231en_activity_relevance, cd6231en_order_sequence [EXTRACTED 1.00]
- **Controlled extension: registration, register, backward compatibility, ISO 19135-1 / 19144-4** — cd6231en_extension_process, cd6231en_registration, cd6231en_metalanguage_register, cd6231en_backward_compatibility, cd6231en_iso_19135, cd6231en_iso_19144_4 [EXTRACTED 1.00]
- **Five progressive descriptions of the same agroforestry parkland (pure LC to comprehensive LC+LU)** — cd6231en_agroforestry_parkland, cd6231en_example_pure_land_cover, cd6231en_example_lc_with_lu, cd6231en_example_pure_land_use, cd6231en_example_lu_with_lc, cd6231en_example_comprehensive [EXTRACTED 1.00]

## Communities (13 total, 0 thin omitted)

### Community 0 - "Agroforestry Examples & LCML Characteristics"
Cohesion: 0.06
Nodes (51): Agroforestry parkland (Sub-Saharan Africa) base example, Example 5: Comprehensive LC+LU representation of parkland agroforestry, Example 2: Land Cover description augmented with Land Use information, Example 4: Land Use description augmented with basic Land Cover attributes, Example 1: Pure Land Cover description of agroforestry parkland, Example 3: Land Use description of agroforestry parkland, ISO 19144-2:2012 (previous edition), LC_AugmentedLandCoverClassDescriptor (+43 more)

### Community 1 - "Registration, Extension & Farming Activities"
Cohesion: 0.06
Nodes (50): Backward compatibility through registration, ISO 19135-1:2015 Procedures for item registration, ISO 19135-1 Procedures for item registration, ISO 19144-4 Registration and Implementation Aspects (under preparation), Revision of the ISO 19144 series (Annex C), ISO/TC 211 Geographic information, Register of legend classes (ISO 19144-1), operationHandling attribute (+42 more)

### Community 2 - "Conformance & Classification System Comparison"
Cohesion: 0.09
Nodes (48): Australian Land Use and Management system (ALUM), Anderson et al. 1976: USGS land use and land cover classification system (Prof. Paper 964), Anderson land use/land cover classification, Annex A Abstract test suite (ATS), Annex B Examples, Annex C Backward compatibility, Antonio Di Gregorio, Building block approach to class description (+40 more)

### Community 3 - "Land Use Functions & Conservation/Heritage"
Cohesion: 0.07
Nodes (35): Five main Land Use functions, IUCN protected area definitions (National Park, 1969), Land Events, Land Functions (Socio-Economic Purposes), Land Use function, LU_ConservationProtectionActivities, LU_ConservationProtectionRestoration, LU_ConservationTypes code list (+27 more)

### Community 4 - "Activity Arrangement & Functional Relationships"
Cohesion: 0.10
Nodes (32): Activity arrangement structure, Activity relevance (1-100 %), UN Central Product Classification (CPC) Version 2.1, 2015, Description Type 2 - Land Use land description, Functional relationship (dominant/secondary/equivalent), Galton 2009: The Water Falls but the Waterfall does not Fall (objects, processes, events), ISO 19103 Conceptual schema language, Land Use activity (+24 more)

### Community 5 - "ISO 19144 Series & Governance"
Cohesion: 0.10
Nodes (25): Application Schema, C Douglas O'Brien, CL_LegendClass (ISO 19144-1), Classification system, Coverage, Discrete coverage, Food and Agriculture Organization of the United Nations (FAO), Fatima Mushtaq (+17 more)

### Community 6 - "Metamodel Descriptors & Test Suite"
Cohesion: 0.16
Nodes (18): Abstract test suite (Annex A), Ambiguity of the term class (UML vs classification), ISO 19105:2022 Conformance and testing, LC_Elements, LC_HorizontalPattern (ISO 19144-2), LC_LandCoverClassDescriptor (ISO 19144-2), LC_LandCoverElementCharacteristic, LC_Stratum (+10 more)

### Community 7 - "Transport, Logistics & Services"
Cohesion: 0.17
Nodes (12): LC_BuiltUpSurface, LC_LinearSurface / LC_LinearSurfaceType, LU_LogisticActivities, LU_LogisticNetwork, LU_LogisticTypes (logisticInfrastructuresServices, storageServices, ...), LU_ProvisionActivities (abstract), LU_ServicesActivities, LU_TransportActivities (+4 more)

### Community 8 - "Heavy Production Industry"
Cohesion: 0.18
Nodes (11): LU_Chemical, LU_Electrical, LU_HeavyEndProductionIndustry, LU_HeavyProductionIndustryActivities (abstract), LU_MachineryProduction, LU_MachineryProductionIndustry, LU_MachineryProductionTypes code list, LU_Mechanical (+3 more)

### Community 9 - "Natural Products Harvesting"
Cohesion: 0.25
Nodes (8): LU_AnimalHuntingTypes code list, LU_Hunting, LU_InlandWaterHarvesting, LU_InlandWaterMarineNaturalProductsHarvesting, LU_MarineHarvesting, LU_NaturalProductsGathering, LU_NaturalProductsPicking, LU_TerrestrialNaturalProductsGathering

### Community 10 - "Buffering & Shielding Activities"
Cohesion: 0.32
Nodes (8): LU_Buffering, LU_BufferingAreaActivities, LU_BufferingShielding, LU_BufferingShieldingActivities (abstract), LU_BufferingTypes code list, LU_Shielding, LU_ShieldingAreaActivities, LU_ShieldingTypes code list

### Community 11 - "Energy Production"
Cohesion: 0.33
Nodes (6): LU_EnergyExtractionActivity, LU_EnergyProduction, LU_EnergyProductionActivity, LU_EnergyProductionIndustryActivities (abstract), LU_EnergyProductionTypes (nuclear, fossilFuel, biomass, hydroElectric, solar, wind, geothermal, tidal, waste, other), LU_OtherEnergyProductionActivity

### Community 12 - "Other / Non-distinct Use"
Cohesion: 0.67
Nodes (3): LU_Insubstantive_Other, LU_NotUnderDistinctUse, LU_OtherUse

## Ambiguous Edges - Review These
- `LU_OilGasExtraction` → `LU_ExtractedMaterialTypes code list`  [AMBIGUOUS]
  cd6231en.pdf · relation: references

## Knowledge Gaps
- **59 isolated node(s):** `Annex B Examples`, `CEN/TC 287`, `C Douglas O'Brien`, `Matieu Henry`, `Fatima Mushtaq` (+54 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 60 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `LU_OilGasExtraction` and `LU_ExtractedMaterialTypes code list`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `Registration of code lists, characteristics and classification systems` connect `Registration, Extension & Farming Activities` to `Agroforestry Examples & LCML Characteristics`, `Conformance & Classification System Comparison`, `Land Use Functions & Conservation/Heritage`, `Activity Arrangement & Functional Relationships`, `Metamodel Descriptors & Test Suite`, `Transport, Logistics & Services`, `Heavy Production Industry`, `Natural Products Harvesting`, `Buffering & Shielding Activities`, `Energy Production`?**
  _High betweenness centrality (0.379) - this node is a cross-community bridge._
- **Why does `LU_Activities` connect `Activity Arrangement & Functional Relationships` to `Agroforestry Examples & LCML Characteristics`, `Registration, Extension & Farming Activities`, `Land Use Functions & Conservation/Heritage`, `Metamodel Descriptors & Test Suite`, `Transport, Logistics & Services`, `Heavy Production Industry`, `Buffering & Shielding Activities`, `Energy Production`?**
  _High betweenness centrality (0.290) - this node is a cross-community bridge._
- **Why does `ISO 19144-2 Land Cover Meta Language (LCML)` connect `Conformance & Classification System Comparison` to `Agroforestry Examples & LCML Characteristics`, `Registration, Extension & Farming Activities`, `Activity Arrangement & Functional Relationships`, `ISO 19144 Series & Governance`, `Metamodel Descriptors & Test Suite`, `Transport, Logistics & Services`?**
  _High betweenness centrality (0.192) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Land Use Meta Language (LUML)` (e.g. with `Three semantic levels: legend, classification system, metalanguage` and `UML 2.5.1 Unified Modelling Language`) actually correct?**
  _`Land Use Meta Language (LUML)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `LU_Activities` (e.g. with `UN Central Product Classification (CPC) Version 2.1, 2015` and `LU_LandUseActivities package`) actually correct?**
  _`LU_Activities` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Annex B Examples`, `CEN/TC 287`, `C Douglas O'Brien` to the rest of the system?**
  _59 weakly-connected nodes found - possible documentation gaps or missing edges._