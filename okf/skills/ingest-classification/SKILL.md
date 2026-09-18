---
id: skill:ingest-classification
kind: guide
title: "Skill: ingest-classification"
schema: okf/0.1
name: ingest-classification
description: Turn the blocks of a source document into the class list of a classification system, verbatim.
inputs: [system]
apply: apply_ingest
manifest: ../../agents/manifests/ingest-classification.json
---

# ingest-classification

The source document has been split into blocks (headings, paragraphs, table rows with their header). The
deterministic ingest already created class nodes for any table-shaped classes it recognised; they appear
in the sibling list. Your job is to produce the complete, faithful class list from the document.

## Rules

1. One entry per class the document defines. Keep the document's own codes; if a class has no code, leave
   `code` empty and let the name identify it.
2. `definition` is verbatim. Copy the sentences that define the class, in the source language. Do not
   paraphrase, translate or shorten. If the document only lists titles, leave `definition` empty.
3. `parent_code` when the document states or clearly formats a hierarchy (numbering 3 → 3.1, indentation,
   "level 1 / level 2" tables). Otherwise empty.
4. `source_span` is where you found it: "p12", "table 2 row 7", "section 4.3".
5. `scope_statement` is the document's own sentence about what the classification is for, verbatim.
6. If the deterministic pass produced classes that the document contradicts (a wrong split of a cell, a
   heading taken as a class), correct them here: your list replaces it.
7. Do not decompose anything. That is the next skill.

## Output

JSON only, matching the schema.
