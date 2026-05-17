# Salt Analysis Simulator — Student Reference Guide

---

> The chemistry reference tables work for both console and web app. Sections marked "Console Version" apply to console only.

## Console Version — Important Notes

- Use **full chemical names** — `dilute hydrochloric acid` not `dil. HCl`, `silver nitrate` not `AgNO3`
- Reagents are **comma separated** — `water, silver nitrate`
- Order doesn't matter — `silver nitrate, water` works the same

---

## Anion Reference

### Dry Tests

| Anion | Reagents | Observation |
|---|---|---|
| acetate | `oxalic acid, water drops` | vinegar smell |
| carbonate | `dilute hydrochloric acid` | brisk effervescence |
| sulphide | `dilute hydrochloric acid` | rotten egg smell |
| sulphite | `dilute hydrochloric acid` | burning sulphur smell |
| nitrite | `dilute hydrochloric acid` | brown fumes |
| chloride | `concentrated hydrochloric acid, heat` | white fumes |
| bromide | `concentrated hydrochloric acid, heat` | brown fumes |
| iodide | `concentrated hydrochloric acid, heat` | violet fumes |
| nitrate | `concentrated hydrochloric acid, copper turnings, heat` | brown fumes |
| sulphate | no dry test — type `cannot guess yet` | no reaction |

### Confirmatory Tests

| Anion | Reagents | Observation |
|---|---|---|
| acetate | `water, ferric chloride` | reddish-brown color |
| carbonate | `water, magnesium sulphate` | milky white precipitate |
| sulphide | `water, lead acetate` | black precipitate |
| sulphite | `water, acidified potassium dichromate` | green color |
| nitrite | `water, oxalic acid, ferrous sulphate` | red color |
| chloride | `water, silver nitrate` | white precipitate |
| bromide | `water, silver nitrate` | pale yellow precipitate |
| iodide | `water, silver nitrate` | yellow precipitate |
| nitrate | `water, ferrous sulphate, concentrated sulphuric acid` | brown ring at the junction of two liquids |
| sulphate | `water, barium chloride` | white precipitate |

---

## Cation Reference

### Wet Tests

| Cation | Group | Reagents | Observation |
|---|---|---|---|
| ammonium | 0 | `concentrated sodium hydroxide, heat` | ammonia smell |
| lead | 1 | `water, dilute hydrochloric acid` | white precipitate |
| copper | 2 | `water, dilute hydrochloric acid, sodium sulphide` | black precipitate |
| ferric | 3 | `water, ammonium chloride, ammonium hydroxide` | reddish-brown precipitate |
| aluminium | 3 | `water, ammonium chloride, ammonium hydroxide` | white precipitate |
| zinc | 4 | `water, ammonium chloride, ammonium hydroxide, sodium sulphide` | white precipitate |
| cobalt | 4 | `water, ammonium chloride, ammonium hydroxide, sodium sulphide` | black precipitate |
| nickel | 4 | `water, ammonium chloride, ammonium hydroxide, sodium sulphide` | black precipitate |
| manganese | 4 | `water, ammonium chloride, ammonium hydroxide, sodium sulphide` | flesh-colored precipitate |
| barium | 5 | `water, ammonium chloride, ammonium hydroxide, ammonium carbonate` | white precipitate |
| calcium | 5 | `water, ammonium chloride, ammonium hydroxide, ammonium carbonate` | white precipitate |
| strontium | 5 | `water, ammonium chloride, ammonium hydroxide, ammonium carbonate` | white precipitate |
| magnesium | 6 | no wet test — type `cannot guess yet` | no reaction |

### Confirmatory Tests

| Cation | Reagents | Observation |
|---|---|---|
| ammonium | `concentrated sodium hydroxide, heat, nessler's reagent` | brown precipitate |
| lead | `water, potassium iodide` | yellow precipitate |
| copper | `water, ammonium hydroxide` | deep blue color |
| ferric | `water, dilute hydrochloric acid, potassium ferrocyanide` | prussian blue color |
| aluminium | `water, dilute hydrochloric acid, blue litmus solution, ammonium hydroxide` | suspended blue precipitate |
| zinc | `water, potassium ferrocyanide` | bluish-white precipitate |
| cobalt | `water, potassium nitrite, ammonium hydroxide` | yellow precipitate |
| nickel | `water, sodium hydroxide, bromine water` | black precipitate |
| manganese | `water, sodium hydroxide` | white precipitate |
| barium | `water, potassium chromate` | yellow precipitate |
| calcium | `water, ammonium oxalate` | white precipitate |
| strontium | `water, ammonium sulphate` | white precipitate |
| magnesium | `water, ammonium chloride, ammonium hydroxide, diammonium hydrogen phosphate` | white precipitate |

---

## Console Version — Accepted Inputs

| Prompt | Acceptable inputs |
|---|---|
| Phase selection | `anion` `cation` |
| Cannot decide yet | `cannot guess yet` |
| Feedback prompt | `yes` `no` |
| Anion names | `acetate` `carbonate` `sulphide` `sulphite` `nitrite` `chloride` `bromide` `iodide` `nitrate` `sulphate` |
| Cation names | `ammonium` `lead` `copper` `ferric` `aluminium` `zinc` `cobalt` `nickel` `manganese` `barium` `calcium` `strontium` `magnesium` |
