import streamlit as st
#import logic
#import random

#for multi user, took help from ai (idk this stuff)
import importlib.util
import uuid

anions = ("acetate",
           "carbonate", "sulphide", "sulphite", "nitrite",
           "chloride", "bromide", "iodide", "nitrate",
           "sulphate")

cations = ("ammonium",
            "lead", "copper",
            "ferric", "aluminium",
            "zinc", "cobalt", "nickel", "manganese",
            "barium", "calcium", "strontium", 
            "magnesium")

st.set_page_config(page_title="Salt Analysis Simulator", layout="centered")

#session states i.e. global variable

#for multi user, took help from ai (idk this stuff)
#it generates a unique id for each user and stores it in session state, so that the state is maintained separately for each user.
if "logic" not in st.session_state:
    module_name = f"logic_{uuid.uuid4().hex}"

    spec = importlib.util.spec_from_file_location(
        module_name,
        "logic.py"
    )

    logic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(logic)

    st.session_state["logic"] = logic

logic = st.session_state["logic"]

if "selected_reagents" not in st.session_state:
    st.session_state["selected_reagents"] = []

if "curr_state" not in st.session_state:
    st.session_state["curr_state"] = "start"

def start_screen():

    #logo(used as image, i didn't draw)
    with st.container(horizontal=True,horizontal_alignment="center"):
        st.image("images/logo.svg")
    
    #all the texts
    st.title("Salt Analysis Simulator",
            text_alignment="center")
    
    st.caption("CLASS 11 & 12 CHEMISTRY",
                text_alignment="center")
    
    st.caption("Practice qualitative salt analysis the way you would in a real lab — reagents, observations, and all.",
               text_alignment="center")
    st.space("xsmall")

    #buttons - start and ref to github(later to pdf if i want)
    with st.container(horizontal=True,horizontal_alignment="center",gap="large"):
        start = st.button("Start Practice")
        #if start button is clicked move to choosing phase screen
        if start:
            st.session_state["curr_state"] = "choosing_phase"
            st.rerun()
    
        st.link_button("Reference Guide",
                    url="https://github.com/ShibamKaran/qualitative-salt-analysis-simulator/blob/main/HOW_TO_PLAY.md",
                    icon="🔗")
    st.space("xsmall")
    st.caption("Built for students preparing for practical exams",
               text_alignment="center")


def phase_selection_screen():
    st.title("CHOOSE A PHASE",
             text_alignment="center")
    st.markdown(":gray[Complete both phases to identify the salt. You can do either one first.]",
               text_alignment="center")
    st.divider()
    st.space("medium")
    with st.container(horizontal=True, horizontal_alignment="center"):
        if logic.anion_complete:
            st.success("**Anion — Acid Radical**  \n\n:small[Dry test + Confirmatory test]   \n\n**✓ Complete**")
        elif not logic.anion_complete:
            with st.container(horizontal_alignment='center',border=True):
                st.markdown("**Anion — Acid Radical**  \n\n:small[Dry test + Confirmatory test]")
                if st.button("Start Anion Analysis", width="stretch"):
                    st.session_state["curr_state"] = "awaiting_dry_test"
                    st.rerun()

        if logic.cation_complete:
            st.success("**Cation — Basic Radical**  \n\n:small[Wet test + Confirmatory test]  \n\n**✓ Complete**")
        elif not logic.cation_complete:
            with st.container(horizontal_alignment='center',border=True):
                st.markdown("**Cation — Basic Radical**  \n\n:small[Wet test + Confirmatory test]")
                if st.button("Start Cation Analysis", width="stretch"):
                    st.session_state["curr_state"] = "awaiting_wet_test"
                    st.rerun()

def draw_reagent_button(reagent_name, reagent_symbol, reagent_bottle_color):
    with st.container(border=True,horizontal_alignment="center",gap ="xxsmall"):
        st.image(f"images/reagents/bottle_{reagent_bottle_color}.svg",width=30)
        if reagent_symbol == None:
            reagent_symbol = reagent_name.title()

        st.caption(reagent_symbol, text_alignment="center")
        if st.button("Added" if reagent_name in st.session_state["selected_reagents"] else "Add",
                     disabled= reagent_name in st.session_state["selected_reagents"],
                     key=f"{reagent_name}_btn"):
            st.session_state["selected_reagents"].append(reagent_name)
            st.rerun()

def anion_dry_test_screen():
    st.title("ANION -- DRY TEST",
             text_alignment="center")
    st.markdown(":gray[Select reagents and perform test]",
               text_alignment="center")
    st.divider()

    reag_col,tube_col,obs_col = st.columns([2,1,1],gap="medium")

    logic.dry_test_observation = "" #reset observation for new test
    #print(st.session_state["selected_reagents"])
    with reag_col:
        st.subheader("Select Reagents")
        col1, col2, col3 = st.columns(3,gap="xxsmall")
        with col1:
            #oxalic acid, conc hcl
            draw_reagent_button("oxalic acid", None, "grey")
            draw_reagent_button("concentrated hydrochloric acid", "Conc. HCl", "yellow")
            
        with col2:
            #water drops, copper turnings
            draw_reagent_button("water drops", None, "blue")

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/copper_turnings.svg",width=60)
                st.caption("Copper Turnings",text_alignment="center")
                if st.button("Added" if "copper turnings" in st.session_state["selected_reagents"] else "Add",
                            disabled= "copper turnings" in st.session_state["selected_reagents"],
                            key = "copper_turnings_btn"):
                        
                    st.session_state["selected_reagents"].append("copper turnings")
                    st.rerun()
            
        with col3:
            #dil hcl, heat
            draw_reagent_button("dilute hydrochloric acid", "Dil. HCl", "green")

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/heat.svg",width=30)
                st.caption("Heat",text_alignment="center")
                if st.button("Added" if "heat" in st.session_state["selected_reagents"] else "Add",
                            disabled= "heat" in st.session_state["selected_reagents"],
                            key = "heat_btn"):
                    
                    st.session_state["selected_reagents"].append("heat")
                    st.rerun()  

        #perform test and get result from logic
        with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
            if st.button("Perform Test", disabled = len(st.session_state["selected_reagents"])==0, width=140):
                logic.dry_test_observation, st.session_state["curr_state"] = logic.handle_action("awaiting_dry_test", tuple(st.session_state["selected_reagents"]))
                st.session_state["selected_reagents"] = []
                
            if st.button("Reset Test",width=140,type="primary"):
                st.session_state["selected_reagents"] = []
                st.rerun()
        
    with obs_col:
        st.subheader("Observation")
        if logic.dry_test_observation != "no reaction":
            st.success(logic.dry_test_observation.title())
        else:
            st.error(logic.dry_test_observation.title())

    with tube_col:
        st.subheader("Test Tube",text_alignment="right")
        if "smell" in logic.dry_test_observation:
            st.image("images/test_tubes/no reaction.svg")
        elif logic.dry_test_observation != "":
            st.image(f"images/test_tubes/{logic.dry_test_observation}.svg")
        else:
            st.image("images/test_tubes/salt.svg")
        
def anion_dry_test_interpretation_screen():
    st.title("WHAT DOES THIS SUGGEST?", text_alignment="center")
    st.markdown(":gray[Based on the observation, guess which anion might be present]",
                text_alignment="center")
    st.divider()

    st.info("Observation: " + logic.dry_test_observation.title())

    st.markdown("**The anion which might be present is --**")
    anion_dry_guess = st.selectbox("**The anion which might be present is --**",options=anions,
                 label_visibility="collapsed",
                 index = None)

    with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
        msg = ""
        if st.button("Cannot Guess Yet", width = "stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action("interpreting_dry_test", "cannot guess yet")
        
        if st.button("Move To Confirmatory Test",
                      disabled = anion_dry_guess == None, icon="➡️",
                      icon_position="right", width="stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action("interpreting_dry_test", anion_dry_guess)
            st.rerun()
    
    st.info(msg)
    if msg == "Let's do another dry test!":
        st.button("Perform Another Dry Test", icon="🔄", icon_position="right")

def anion_confirmatory_test_screen():
    st.title("ANION -- CONFIRMATORY TEST",
             text_alignment="center")
    st.markdown(":gray[Select reagents and perform test]",
               text_alignment="center")
    st.divider()

    reag_col,tube_col,obs_col = st.columns([2,1,1],gap="medium")
    logic.anion_confirmatory_observation = "" #reset observation for new test
    #print(st.session_state["selected_reagents"])
    with reag_col:
        st.subheader("Select Reagents")
        col1, col2, col3 = st.columns(3,gap="xxsmall")
        with col1:
            #water, ferric chloride, ferrous sulphate, barium chloride
            draw_reagent_button("water", None, "blue")
            draw_reagent_button("ferric chloride", "FeCl₃", "purple")
            draw_reagent_button("ferrous sulphate", "FeSO₄", "pink")
            draw_reagent_button("barium chloride", "BaCl₂", "blue")     
            
        with col2:
            #magnesium sulphate, lead acetate, silver nitrate
            draw_reagent_button("magnesium sulphate", "MgSO₄", "grey")
            draw_reagent_button("lead acetate", None, "green")
            draw_reagent_button("silver nitrate", "AgNO₃", "orange")
       
        with col3:
            #acidified potassium dichromate, oxalic acid, conc h2so4
            draw_reagent_button("acidified potassium dichromate", "Acid.K₂Cr₂O₇", "orange")
            draw_reagent_button("oxalic acid", None, "darkblue")
            draw_reagent_button("concentrated sulphuric acid", "Conc. H₂SO₄", "yellow")

        #perform test and get result from logic
        with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
            if st.button("Perform Test", disabled = len(st.session_state["selected_reagents"])==0, width=140):
                logic.anion_confirmatory_observation, st.session_state["curr_state"] = logic.handle_action("awaiting_confirmatory_test", tuple(st.session_state["selected_reagents"]))
                st.session_state["selected_reagents"] = []
                
            if st.button("Reset Test",width=140,type="primary"):
                st.session_state["selected_reagents"] = []
                st.rerun()
        
    with obs_col:
        st.subheader("Observation")
        if logic.anion_confirmatory_observation != "no reaction":
            st.success(logic.anion_confirmatory_observation.title())
        else:
            st.error(logic.anion_confirmatory_observation.title())

    with tube_col:
        st.subheader("Test Tube",text_alignment="right")
        if "smell" in logic.anion_confirmatory_observation:
            st.image("images/test_tubes/no reaction.svg")
        elif logic.anion_confirmatory_observation != "":
            st.image(f"images/test_tubes/{logic.anion_confirmatory_observation}.svg")
        else:
            st.image("images/test_tubes/salt.svg")     

def anion_confirmatory_test_interpretation_screen():
    st.title("WHAT DOES THIS SUGGEST?", text_alignment="center")
    st.markdown(":gray[Based on the observation, guess which anion is present]",
                text_alignment="center")
    st.divider()

    st.info("Observation: " + logic.anion_confirmatory_observation.title())

    st.markdown("**The anion present and confirmed is --**")
    anion_confirmatory_guess = st.selectbox("**The anion present and confirmed is --**",options=anions,
                 label_visibility="collapsed",
                 index = None)

    with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
        msg = ""
        if st.button("Finish Anion Analysis",
                      disabled = anion_confirmatory_guess == None, icon="✅",
                      icon_position="right", width="stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action("interpreting_confirmatory_test", anion_confirmatory_guess)
    
    if msg == "Incorrect guess!":
        st.rerun()
    else:
        st.success(msg)

def feedback_screen(confirmatory_obs,feedback_type = "feedback"): 
    #default anion - just for safety
    # feedback type can be "feedback" or "feedback_cation"
    st.title("FEEDBACK", text_alignment="center")
    st.divider()
    st.error("Incorrect guess! / Incorrect test performed!")
    st.subheader("Would you like feedback?")
    with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
        msg = ""
        if st.button("Yes - Show Feedback!",width="stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action(feedback_type, "yes", confirmatory_obs)
        if st.button("No - End Phase",width="stretch",type="primary"):
            msg, st.session_state["curr_state"] = logic.handle_action(feedback_type, "no", confirmatory_obs)
        
    st.warning(msg)

def cation_wet_test_screen():
    st.title("CATION -- WET TEST",
             text_alignment="center")
    st.markdown(":gray[Select reagents and perform test]",
               text_alignment="center")
    st.divider()
    reag_col,tube_col,obs_col = st.columns([2,1,1],gap="medium")
    logic.wet_test_observation = "" #reset observation for new test
    with reag_col:
        st.subheader("Select Reagents")
        col1, col2, col3 = st.columns(3,gap="xxsmall")
        with col1:
            #water, conc. sodium hydroxide, ammonium carbonate
            draw_reagent_button("water", None, "blue")
            draw_reagent_button("concentrated sodium hydroxide", "Conc. NaOH", "yellow")
            draw_reagent_button("ammonium carbonate", "(NH₄)₂CO₃", "grey")
        
        with col2:
            #ammonium chloride, ammonium hydroxide, heat
            draw_reagent_button("ammonium chloride", "NH₄Cl", "grey")
            draw_reagent_button("ammonium hydroxide", "NH₄OH", "purple")

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/heat.svg",width=30)
                st.caption("Heat",text_alignment="center")
                if st.button("Added" if "heat" in st.session_state["selected_reagents"] else "Add",
                            disabled= "heat" in st.session_state["selected_reagents"],
                            key = "heat_btn_cation"):
                    
                    st.session_state["selected_reagents"].append("heat")
                    st.rerun()
   
        with col3:
            #dil hcl, sodium sulphide
            draw_reagent_button("dilute hydrochloric acid", "Dil. HCl", "green")
            draw_reagent_button("sodium sulphide", "Na₂S", "orange")

        #perform test and get result from logic
        with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
            if st.button("Perform Test", disabled = len(st.session_state["selected_reagents"])==0, width=140):
                logic.wet_test_observation, st.session_state["curr_state"] = logic.handle_action("awaiting_wet_test", tuple(st.session_state["selected_reagents"]))
                st.session_state["selected_reagents"] = []
                
            if st.button("Reset Test",width=140,type="primary"):
                st.session_state["selected_reagents"] = []
                st.rerun()
        
    with obs_col:
        st.subheader("Observation")
        if logic.wet_test_observation != "no reaction":
            st.success(logic.wet_test_observation.title())
        else:
            st.error(logic.wet_test_observation.title())
    
    with tube_col:
        st.subheader("Test Tube",text_alignment="right")
        if "smell" in logic.wet_test_observation:
            st.image("images/test_tubes/no reaction.svg")
        elif logic.wet_test_observation != "":
            st.image(f"images/test_tubes/{logic.wet_test_observation}.svg")
        else:
            st.image("images/test_tubes/salt.svg")

def cation_wet_test_interpretation_screen():
    st.title("WHAT DOES THIS SUGGEST?", text_alignment="center")
    st.markdown(":gray[Based on the observation, guess which cation/s might be present]",
                text_alignment="center")
    st.divider()

    st.info("Observation: " + logic.wet_test_observation.title())

    st.markdown("**The cation/s which might be present is/are --**")
    cation_wet_guess = st.multiselect("**The cation/s which might be present is/are --**",options=cations,
                 label_visibility="collapsed")

    with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
        msg = ""
        if st.button("Cannot Guess Yet", width = "stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action("interpreting_wet_test", ("cannot guess yet",))
        
        if st.button("Move To Confirmatory Test",
                      disabled = cation_wet_guess == [], icon="➡️",
                      icon_position="right", width="stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action("interpreting_wet_test", tuple(cation_wet_guess))
            st.rerun()
    
    st.info(msg)
    if msg == "Let's do another wet test!":
        st.button("Perform Another Wet Test", icon="🔄", icon_position="right")

def cation_confirmatory_test_screen():
    st.title("CATION -- CONFIRMATORY TEST",
             text_alignment="center")
    st.markdown(":gray[Select reagents and perform test]",
               text_alignment="center")
    st.divider()

    reag_col,tube_col,obs_col = st.columns([2,1,1],gap="medium")
    logic.cation_confirmatory_observation = "" #reset observation for new test
    with reag_col:
        st.subheader("Select Reagents")
        col1, col2, col3 = st.columns(3,gap="xxsmall")
        with col1:
            #water, Potassium nitrite, conc Sodium hydroxide, Ammonium Oxalate, Potassium chromate
            draw_reagent_button("water", None, "blue")
            draw_reagent_button("potassium nitrite", "KNO₂", "orange")
            draw_reagent_button("concentrated sodium hydroxide", "conc. NaOH", "yellow")
            draw_reagent_button("ammonium oxalate", "(NH₄)₂C₂O₄", "green")
            draw_reagent_button("potassium chromate", "K₂CrO₄", "darkblue")
        
        with col2:
            #potassium iodide, dmg solution, dil hcl, Ammonium sulphate, Sodium hydroxide
            draw_reagent_button("potassium iodide", "KI", "grey")
            draw_reagent_button("DMG solution", "DMG sol.", "pink")
            draw_reagent_button("dilute hydrochloric acid", "Dil. HCl", "green")
            draw_reagent_button("ammonium sulphate", "(NH₄)₂SO₄", "grey")
            draw_reagent_button("sodium hydroxide", "NaOH", "yellow")

        with col3:
            #ammonium hydroxide, potassium ferrocyanide, Blue litmus solution, diammonium hydrogen phosphate, Nessler's reagent
            draw_reagent_button("ammonium hydroxide", "NH₄OH", "purple")
            draw_reagent_button("potassium ferrocyanide", "K₄[Fe(CN)₆]", "grey")
            draw_reagent_button("blue litmus solution", "Blue Lit. Sol.", "darkblue")
            draw_reagent_button("diammonium hydrogen phosphate", "(NH₄)₂HPO₄", "orange")
            draw_reagent_button("nessler's reagent", "Nessler rea.", "yellow")

        #perform test and get result from logic
        with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
            if st.button("Perform Test", disabled = len(st.session_state["selected_reagents"])==0, width=140):
                logic.cation_confirmatory_observation, st.session_state["curr_state"] = logic.handle_action("awaiting_confirmatory_test_cation", tuple(st.session_state["selected_reagents"]))
                st.session_state["selected_reagents"] = []
                
            if st.button("Reset Test",width=140,type="primary"):
                st.session_state["selected_reagents"] = []
                st.rerun()
    with obs_col:
        st.subheader("Observation")
        if logic.cation_confirmatory_observation != "no reaction":
            st.success(logic.cation_confirmatory_observation.title())
        else:
            st.error(logic.cation_confirmatory_observation.title())
    with tube_col:
        st.subheader("Test Tube",text_alignment="right")
        if "smell" in logic.cation_confirmatory_observation:
            st.image("images/test_tubes/no reaction.svg")
        elif logic.cation_confirmatory_observation != "":
            st.image(f"images/test_tubes/{logic.cation_confirmatory_observation}.svg")
        else:
            st.image("images/test_tubes/salt.svg")
      
def cation_confirmatory_test_interpretation_screen():
    st.title("WHAT DOES THIS SUGGEST?", text_alignment="center")
    st.markdown(":gray[Based on the observation, guess which cation is present]",
                text_alignment="center")
    st.divider()

    st.info("Observation: " + logic.cation_confirmatory_observation.title())

    st.markdown("**The cation present and confirmed is --**")
    cation_confirmatory_guess = st.selectbox("**The cation present and confirmed is --**",options=cations,
                 label_visibility="collapsed", index = None)
            
    
    with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
        msg = ""
        if st.button("Cannot Guess Yet", width = "stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action("interpreting_confirmatory_test_cation", "cannot guess yet")

        if st.button("Finish Cation Analysis",
                      disabled = cation_confirmatory_guess == None, icon="✅",
                      icon_position="right", width="stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action("interpreting_confirmatory_test_cation", cation_confirmatory_guess)
    
    if msg == "Incorrect guess!":
        st.rerun()
    elif msg == "Let's do another confirmatory test!":
        st.info(msg)
    else:
        st.success(msg)

    if msg == "Let's do another confirmatory test!":
        st.button("Perform Another Confirmatory Test", icon="🔄", icon_position="right")    

def final_screen():
    st.balloons()
    st.title("SALT ANALYSIS COMPLETE!", text_alignment="center")
    st.divider()

    st.subheader("The salt given to you was --", text_alignment="center")

    #i dont know html, i used ai to generate this, and it worked on first try, so im not changing it :P
    st.markdown(
        f"""
        <div style="text-align:center;">
            <div style="
                display:inline-block;
                background-color:#15803d;
                padding:18px 28px;
                border-radius:14px;
                color:white;
                font-size:28px;
                font-weight:bold;
            ">
                {logic.cation.title()} {logic.anion.title()}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.space("small")

    with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
        if st.button("Start New Analysis", icon="🔄", icon_position="right"):
            st.session_state.clear()
            st.rerun()
    
        if st.button("Balloons Again!", icon="🎈", icon_position="right"):
            st.balloons()


def main():
    if logic.anion_complete and logic.cation_complete:
        final_screen()
    elif st.session_state["curr_state"] == "start":
        start_screen()
    elif st.session_state["curr_state"] == "choosing_phase":
        phase_selection_screen()
    elif st.session_state["curr_state"] == "awaiting_dry_test":
        anion_dry_test_screen()
    elif st.session_state["curr_state"] == "interpreting_dry_test":
        anion_dry_test_interpretation_screen()
    elif st.session_state["curr_state"] == "awaiting_confirmatory_test":
        anion_confirmatory_test_screen()
    elif st.session_state["curr_state"] == "interpreting_confirmatory_test":
        anion_confirmatory_test_interpretation_screen()
    elif st.session_state["curr_state"] == "feedback":
        feedback_screen(logic.anion_confirmatory_observation,"feedback")
    elif st.session_state["curr_state"] == "feedback_cation":
        feedback_screen(logic.cation_confirmatory_observation,"feedback_cation")
    elif st.session_state["curr_state"] == "awaiting_wet_test":
        cation_wet_test_screen()
    elif st.session_state["curr_state"] == "interpreting_wet_test":
        cation_wet_test_interpretation_screen()
    elif st.session_state["curr_state"] == "awaiting_confirmatory_test_cation":
        cation_confirmatory_test_screen()
    elif st.session_state["curr_state"] == "interpreting_confirmatory_test_cation":
        cation_confirmatory_test_interpretation_screen()

main()
