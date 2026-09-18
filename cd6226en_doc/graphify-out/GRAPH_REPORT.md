# Graph Report - cd6226en_doc  (2026-09-17)

## Corpus Check
- Corpus is ~0 words - fits in a single context window. You may not need a graph.

## Summary
- 108 nodes · 198 edges · 9 communities
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 8 edges (avg confidence: 0.8)
- Token cost: 100,000 input · 14,610 output

## Community Hubs (Navigation)
- Coverage & Classified Surface Model
- Classification Systems & LCCS Lineage
- Classification Registers & Rules
- Classifier, Legend & Concept Dictionaries
- Classification Data Sets & Metadata
- Conformance & Abstract Test Suite
- Feature Types & General Feature Model
- Features & Classified Objects
- ISO/TC 211 Governance

## God Nodes (most connected - your core abstractions)
1. `ISO 19144-1:2009 Classification System Structure` - 25 edges
2. `Classification system` - 12 edges
3. `ISO 19135:2005 Procedures for item registration` - 10 edges
4. `Land Cover Classification System (LCCS)` - 9 edges
5. `Legend` - 9 edges
6. `ISO 19144 series Geographic information - Classification systems` - 8 edges
7. `Discrete coverage` - 8 edges
8. `CL_ClassificationRegister` - 8 edges
9. `CV_Coverage` - 8 edges
10. `Classifier` - 7 edges

## Surprising Connections (you probably didn't know these)
- `A posteriori classification` --conceptually_related_to--> `Legend`  [INFERRED]
  cd6226en.pdf → cd6226en.pdf  _Bridges community 3 → community 1_
- `Mixed classification (A|B)` --conceptually_related_to--> `Legend`  [INFERRED]
  cd6226en.pdf → cd6226en.pdf  _Bridges community 3 → community 2_
- `CL_ClassificationRulesClass` --cites--> `ISO 19144-1:2009 Classification System Structure`  [EXTRACTED]
  cd6226en.pdf → cd6226en.pdf  _Bridges community 5 → community 2_
- `ISO 19144-1:2009 Classification System Structure` --references--> `Annex B A priori and a posteriori classification systems`  [EXTRACTED]
  cd6226en.pdf → cd6226en.pdf  _Bridges community 5 → community 1_
- `ISO 19144-1:2009 Classification System Structure` --cites--> `ISO 19101 Reference model`  [EXTRACTED]
  cd6226en.pdf → cd6226en.pdf  _Bridges community 5 → community 7_

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **CL classification register schema (ISO 19135 extension)** — cd6226en_cl_classificationregister, cd6226en_cl_classificationlegenditem, cd6226en_cl_classificationruleitem, cd6226en_cl_classificationlegendclass, cd6226en_cl_classificationrulesclass, cd6226en_re_register, cd6226en_re_registeritem, cd6226en_re_itemclass [EXTRACTED 1.00]
- **Discrete coverage representation of classification results** — cd6226en_cv_coverage, cd6226en_cv_discretecoverage, cd6226en_cv_discretesurfacecoverage, cd6226en_cv_geometryvaluepair, cd6226en_cv_surfacevaluepair, cd6226en_cl_classifiedsurface, cd6226en_cl_tessellationgeometry, cd6226en_gm_surface [EXTRACTED 1.00]
- **Classification / legend / classifier conceptual core** — cd6226en_classification_system, cd6226en_classification, cd6226en_classifier, cd6226en_legend, cd6226en_legend_class, cd6226en_classified_object [EXTRACTED 1.00]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Coverage & Classified Surface Model"
Cohesion: 0.11
Nodes (27): CL_ClassifiedSurface, CL_TessellationGeometry (code list), Coverage, CV_AttributeValues, CV_Coverage, CV_DiscreteCoverage, CV_DiscreteSurfaceCoverage, CV_DomainObject (+19 more)

### Community 1 - "Classification Systems & LCCS Lineage"
Cohesion: 0.18
Nodes (18): A posteriori classification, A priori classification, Annex B A priori and a posteriori classification systems, Antonio Di Gregorio, Braun-Blanquet method (floristic vegetation classification), C Douglas O'Brien, Classification system, Food and Agriculture Organization of the United Nations (FAO) (+10 more)

### Community 2 - "Classification Registers & Rules"
Cohesion: 0.18
Nodes (18): CL_ClassificationLegendItem, CL_ClassificationRegister, CL_ClassificationRuleItem, CL_ClassificationRulesClass, Classification rule, Cross-referencing between classifier registers, Identifier, ISO 19135:2005 Procedures for item registration (+10 more)

### Community 3 - "Classifier, Legend & Concept Dictionaries"
Cohesion: 0.24
Nodes (11): CL two-letter UML prefix convention, Classification, Classifier, Concept dictionary register for a classification scheme, Feature catalogue, Feature concept dictionary, ISO 19126 Feature concept dictionaries and registers, Legend (+3 more)

### Community 4 - "Classification Data Sets & Metadata"
Cohesion: 0.27
Nodes (10): CL_ClassificationCollection, CL_DataSet, Classification data set, DS_DataSet, EX_Extent, ISO 19115 Metadata, ISO 19115-2 Metadata - Extensions for imagery and gridded data, ISO/TS 19129 Imagery, gridded and coverage data framework (+2 more)

### Community 5 - "Conformance & Abstract Test Suite"
Cohesion: 0.31
Nodes (9): Annex A Abstract test suite, CL_ClassificationLegendClass, Three conformance classes, functionalLanguage attribute, ISO 19108 Temporal schema, ISO 19110:2005 Methodology for feature cataloguing, ISO 19144-1:2009 Classification System Structure, ISO/IEC 13211-1 Prolog (+1 more)

### Community 6 - "Feature Types & General Feature Model"
Cohesion: 0.29
Nodes (7): CL_FeatureTypeReference, CL_LegendClass, Feature type, GF_AttributeType, GF_FeatureType, ISO 19109:2005 Rules for application schema (General Feature Model), A.2 Conformance of a classification system

### Community 7 - "Features & Classified Objects"
Cohesion: 0.67
Nodes (4): Classified object, Feature, Feature attribute, ISO 19101 Reference model

### Community 8 - "ISO/TC 211 Governance"
Cohesion: 0.50
Nodes (4): International Organization for Standardization (ISO), ISO/TC 211 Geographic information/Geomatics, ISO TC211 Advisory Group 13 on land cover and land use, Matieu Henry

## Knowledge Gaps
- **9 isolated node(s):** `International Organization for Standardization (ISO)`, `C Douglas O'Brien`, `Matieu Henry`, `Fatima Mushtaq`, `John Latham` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 9 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ISO 19144-1:2009 Classification System Structure` connect `Conformance & Abstract Test Suite` to `Coverage & Classified Surface Model`, `Classification Systems & LCCS Lineage`, `Classification Registers & Rules`, `Classifier, Legend & Concept Dictionaries`, `Classification Data Sets & Metadata`, `Feature Types & General Feature Model`, `Features & Classified Objects`?**
  _High betweenness centrality (0.532) - this node is a cross-community bridge._
- **Why does `ISO 19144 series Geographic information - Classification systems` connect `Classification Systems & LCCS Lineage` to `ISO/TC 211 Governance`, `Conformance & Abstract Test Suite`?**
  _High betweenness centrality (0.151) - this node is a cross-community bridge._
- **Why does `Discrete coverage` connect `Coverage & Classified Surface Model` to `Classification Systems & LCCS Lineage`, `Classifier, Legend & Concept Dictionaries`, `Classification Data Sets & Metadata`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Classification system` (e.g. with `Land Cover Classification System (LCCS)` and `Land Cover Meta Language (LCML) ISO 19144-2`) actually correct?**
  _`Classification system` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Land Cover Classification System (LCCS)` (e.g. with `Classification system` and `Hierarchical classification system`) actually correct?**
  _`Land Cover Classification System (LCCS)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Legend` (e.g. with `A posteriori classification` and `Mixed classification (A|B)`) actually correct?**
  _`Legend` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `International Organization for Standardization (ISO)`, `C Douglas O'Brien`, `Matieu Henry` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._