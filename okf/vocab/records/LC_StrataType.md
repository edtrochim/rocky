---
id: record:LC_StrataType
kind: vocab_record
title: LC_StrataType
sources:
- lchs.xsd
fields:
- HPID
- stratumID
- description
- presenceType
- portioning
- onTop
- onTopType
- order
schema: okf/0.1
---

# LC_StrataType

Vertical strata layers within horizontal patterns

## Fields

| property | type | values / range | required | meaning |
|---|---|---|---|---|
| `HPID` | xs:string |  | yes |  |
| `stratumID` | xs:string |  | yes |  |
| `description` | xs:string |  |  |  |
| `presenceType` | PresenceTypeEnum | `Fixed`, `Exclusive`, `Conditional Temporal`, `Precluded`, `Mandatory`, `Temporal Sequence Depending` |  |  |
| `portioning` | xs:decimal | min, max |  |  |
| `onTop` | xs:string |  |  |  |
| `onTopType` | xs:string |  |  |  |
| `order` | xs:integer |  |  |  |
