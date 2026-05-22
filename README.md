# Qualitative Salt Analysis Simulator

An interactive simulator that helps students practice qualitative salt analysis practicals — the way they would in a real lab.

## What it does
Students are given an unknown salt and must identify both the acid radical (anion) and basic radical (cation) by performing the correct chemical tests in sequence. The simulator evaluates not just the final answer but the entire reasoning process — wrong reagents give no reaction, and feedback is provided based on where the student went wrong.

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
- Logic layer separated and ready for GUI development
- Streamlit web app but only one user can play at a time (multi user soon)
  
## Python files
- `logic.py` — core logic layer: chemistry data, state machine, test evaluator. No display code.
- `console.py` — console interface: imports from logic.py, handles terminal interaction.
- `main.py` — original version, preserved for reference.
- `app.py` — Streamlit web app

## How to Run

### Console version
Requires Python 3 and `logic.py` in the same folder.

**Mac/Linux:** `python3 main.py` or `python3 console.py`  
**Windows:** `python main.py` or `python console.py`

### Web app
https://qualitative-salt-analysis-simulator.streamlit.app

## Planned
- Multiple user can use at same time without messing with eachother

## Tech Stack
- **Language**: Python
- **Console version**: Built-in Python only
- **Web app**: Streamlit
- **Deployment**: Streamlit Cloud (free)
