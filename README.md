# Qualitative Salt Analysis Simulator

An interactive simulator that helps students practice qualitative salt analysis practicals — the way they would in a real lab.

## Website

🔗 [salt-analysis-simulator.streamlit.app](https://salt-analysis-simulator.streamlit.app)

## What it does
Students are given an unknown salt and must identify both the acid radical (anion) and basic radical (cation) by performing the correct chemical tests in sequence. The simulator evaluates not just the final answer but the entire reasoning process — wrong reagents give no reaction, and feedback is provided based on where the student went wrong.

## Who it's for
School students (Class 11/12) preparing for chemistry practical exams, particularly those following the CBSE syllabus.

## What makes it different
- **Decision-based** — reagent choices affect outcomes, wrong reagents give no reaction
- **Thinking layer** — students must interpret observations before proceeding
- **Targeted feedback** — feedback identifies specifically where reasoning went wrong
- **Realistic flow** — mirrors the actual lab procedure students follow in exams
  
## Covers

- 10 anions — acetate, carbonate, sulphide, sulphite, nitrite, chloride, bromide, 
  iodide, nitrate, sulphate
- 13 cations — ammonium, lead, copper, ferric, aluminium, zinc, cobalt, nickel, 
  manganese, barium, calcium, strontium, magnesium
  
## Python files
- `logic.py` — core logic layer: chemistry data, state machine, test evaluator. Has class Logic.
- `console.py` — console interface: imports from logic.py, handles terminal interaction.
- `main.py` — original version, preserved for reference.
- `app.py` — Streamlit web app

## How to Run

### Console version
Requires Python 3 and `logic.py` in the same folder.

**Mac/Linux:** `python3 main.py` or `python3 console.py`  
**Windows:** `python main.py` or `python console.py`

### Web app
https://salt-analysis-simulator.streamlit.app

## Planned
- Add colored salt images in test tube.

## Tech Stack
- **Language**: Python
- **Console version**: Built-in Python only
- **Web app**: Streamlit 1.57.0
- **Deployment**: Streamlit Cloud (free)

## Reference

See [HOW_TO_PLAY.md](HOW_TO_PLAY.md) for a guide on how to use the simulator.

## Credits

### Images (.SVG Files)
- Reagent bottle images — generated using Claude (Anthropic)
- Test tube images — generated using Gemini (Google)

---
*All chemistry logic, app structure, and overall design were built by me(Shibam Karan). 
AI tools were used for specific assets mentioned above under credits. (I like to be transparent about this stuff :P)*
