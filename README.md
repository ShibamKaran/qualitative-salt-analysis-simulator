# Qualitative Salt Analysis Simulator

An interactive simulator that helps students practice qualitative salt analysis practicals — the way they would in a real lab.

## What it does
Students are given an unknown salt and must identify both the acid radical (anion) and basic radical (cation) by performing the correct chemical tests in sequence. The simulator evaluates not just the final answer but the entire reasoning process — wrong reagents give misleading results, and feedback is provided based on where the student went wrong.

## Who it's for
School students (Class 11/12) preparing for chemistry practical exams, particularly those following the CBSE syllabus.

## What makes it different
- **Decision-based** — reagent choices affect outcomes, wrong reagents give no reaction
- **Thinking layer** — students must interpret observations before proceeding
- **Targeted feedback** — feedback identifies specifically where reasoning went wrong
- **Realistic flow** — mirrors the actual lab procedure students follow in exams

## Current State
- Console version complete and tested
- Full anion detection (10 anions) with dry test and confirmatory test
- Full cation detection (13 cations) with wet test and confirmatory test
- State machine architecture ready for GUI transition

## Planned
- Tkinter GUI with separate screens for each phase
- Dropdown menus for reagent selection
- Visual feedback and observations display

## Built with
Python
