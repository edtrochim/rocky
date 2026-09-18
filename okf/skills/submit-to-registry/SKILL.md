---
id: skill:submit-to-registry
kind: guide
title: "Skill: submit-to-registry"
schema: okf/0.1
name: submit-to-registry
description: Draft the message to FAO's Land Cover Legend Registry with the package attached, then stop for a person to send.
inputs: [system]
requires: package built and submission_check ok
---

# submit-to-registry

Only when the run was started with `--submit`. Nothing here sends anything; an agent never contacts
FAO. The output is a drafted message a person reviews and sends.

## Steps

1. Confirm `systems/<slug>/package/` exists and the last `submission_check` was `ok`. If not, stop and
   say what is missing.
2. Write `systems/<slug>/package/SUBMISSION.md` with:
   - To: the LCLR contact (FAO Geospatial Unit, via https://www.fao.org/contact-us/ or the contact given
     on https://data.apps.fao.org/lclr-tool/en/); leave the address for the person to fill in.
   - Subject: "Land cover legend for registration: <system title>".
   - Body: who the publisher is, what the legend is for, the format (LChS, with an LCCS3 copy), the number
     of classes and how many are fully decomposed, the reference document and link, the licence, and the
     list of unresolved items the registrar should know about. Ask which reference and dataset records
     FAO needs and whether a GeoNetwork record exists.
   - Attachments: the package files by name.
3. Append to `SYSTEM.md` run history: `submission drafted <date>`, status `awaiting_send`.
4. Tell the person where the draft is. Do not send it, do not open a mail client, do not post anywhere.
