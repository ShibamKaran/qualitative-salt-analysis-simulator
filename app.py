import streamlit as st
import logic

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


#session states i.e. global variable
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
                st.button("Start Cation Analysis", width="stretch")

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
            with st.container(border=True,horizontal_alignment="center",gap ="xxsmall"):
                st.image("images/reagents/bottle_grey.svg",width=30)
                st.caption("Oxalic Acid",text_alignment="center")
                if st.button("Added ✅" if "oxalic acid" in st.session_state["selected_reagents"] else "Add",  
                                disabled= "oxalic acid" in st.session_state["selected_reagents"],
                                key="oxalic_acid_btn"):
                        
                    st.session_state["selected_reagents"].append("oxalic acid")
                    st.rerun()  

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_yellow.svg",width=30)
                st.caption("Conc. HCl",text_alignment="center")
                if st.button("Added ✅" if "concentrated hydrochloric acid" in st.session_state["selected_reagents"] else "Add",
                            disabled= "concentrated hydrochloric acid" in st.session_state["selected_reagents"],
                            key = "conc_hcl_btn"):
                    
                    st.session_state["selected_reagents"].append("concentrated hydrochloric acid")
                    st.rerun()

            
        with col2:
            #water drops, copper turnings
            with st.container(border=True,horizontal_alignment="center",gap ="xxsmall"):
                st.image("images/reagents/bottle_blue.svg",width=30)
                st.caption("Water Drops",text_alignment="center")
                if st.button("Added ✅" if "water drops" in st.session_state["selected_reagents"] else "Add",  
                            disabled= "water drops" in st.session_state["selected_reagents"],
                            key="water_drops_btn"):
                                            
                    st.session_state["selected_reagents"].append("water drops")
                    st.rerun()

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/copper_turnings.svg",width=60)
                st.caption("Copper Turnings",text_alignment="center")
                if st.button("Added ✅" if "copper turnings" in st.session_state["selected_reagents"] else "Add",
                            disabled= "copper turnings" in st.session_state["selected_reagents"],
                            key = "copper_turnings_btn"):
                        
                    st.session_state["selected_reagents"].append("copper turnings")
                    st.rerun()
            
        with col3:
            #dil hcl, heat
            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_green.svg",width=30)
                st.caption("Dil. HCl",text_alignment="center")
                if st.button("Added ✅" if "dilute hydrochloric acid" in st.session_state["selected_reagents"] else "Add",
                            disabled= "dilute hydrochloric acid" in st.session_state["selected_reagents"],
                            key = "dil_hcl_btn"):
                        
                    st.session_state["selected_reagents"].append("dilute hydrochloric acid")
                    st.rerun()
                
            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/heat.svg",width=30)
                st.caption("Heat",text_alignment="center")
                if st.button("Added ✅" if "heat" in st.session_state["selected_reagents"] else "Add",
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
    st.title("WHAT DOES IT THIS SUGGEST?", text_alignment="center")
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
            with st.container(border=True,horizontal_alignment="center",gap ="xxsmall"):
                st.image("images/reagents/bottle_blue.svg",width=30)
                st.caption("Water",text_alignment="center")
                if st.button("Added ✅" if "water" in st.session_state["selected_reagents"] else "Add",  
                            disabled= "water" in st.session_state["selected_reagents"],
                            key="water_btn"):
                                            
                    st.session_state["selected_reagents"].append("water")
                    st.rerun()

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_purple.svg",width=30)
                st.caption("FeCl₃",text_alignment="center")
                if st.button("Added ✅" if "ferric chloride" in st.session_state["selected_reagents"] else "Add",
                            disabled= "ferric chloride" in st.session_state["selected_reagents"],
                            key = "ferric_chloride_btn"):
                    
                    st.session_state["selected_reagents"].append("ferric chloride")
                    st.rerun()

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_pink.svg",width=30)
                st.caption("FeSO₄",text_alignment="center")
                if st.button("Added ✅" if "ferrous sulphate" in st.session_state["selected_reagents"] else "Add",
                            disabled= "ferrous sulphate" in st.session_state["selected_reagents"],
                            key = "ferrous_sulphate_btn"):
                    
                    st.session_state["selected_reagents"].append("ferrous sulphate")
                    st.rerun()

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_blue.svg",width=30)
                st.caption("BaCl₂",text_alignment="center")
                if st.button("Added ✅" if "barium chloride" in st.session_state["selected_reagents"] else "Add",
                            disabled= "barium chloride" in st.session_state["selected_reagents"],
                            key = "barium_chloride_btn"):
                    
                    st.session_state["selected_reagents"].append("barium chloride")
                    st.rerun()       
            
        with col2:
            #magnesium sulphate, lead acetate, silver nitrate
            with st.container(border=True,horizontal_alignment="center",gap ="xxsmall"):
                st.image("images/reagents/bottle_grey.svg",width=30)
                st.caption("MgSO₄",text_alignment="center")
                if st.button("Added ✅" if "magnesium sulphate" in st.session_state["selected_reagents"] else "Add",  
                            disabled= "magnesium sulphate" in st.session_state["selected_reagents"],
                            key="magnesium_sulphate_btn"):
                                            
                    st.session_state["selected_reagents"].append("magnesium sulphate")
                    st.rerun()

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_green.svg", width=30)
                st.caption("Lead Acetate",text_alignment="center")
                if st.button("Added ✅" if "lead acetate" in st.session_state["selected_reagents"] else "Add",
                            disabled= "lead acetate" in st.session_state["selected_reagents"],
                            key = "lead_acetate_btn"):
                        
                    st.session_state["selected_reagents"].append("lead acetate")
                    st.rerun()

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_orange.svg", width=30)
                st.caption("AgNO₃",text_alignment="center")
                if st.button("Added ✅" if "silver nitrate" in st.session_state["selected_reagents"] else "Add",
                            disabled= "silver nitrate" in st.session_state["selected_reagents"],
                            key = "silver_nitrate_btn"):
                        
                    st.session_state["selected_reagents"].append("silver nitrate")
                    st.rerun()          
        with col3:
            #acidified potassium dichromate, oxalic acid, conc h2so4
            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_orange.svg",width=30)
                st.caption("Acid.K₂Cr₂O₇",text_alignment="center")
                if st.button("Added ✅" if "acidified potassium dichromate" in st.session_state["selected_reagents"] else "Add",
                            disabled= "acidified potassium dichromate" in st.session_state["selected_reagents"],
                            key = "acidified_potassium_dichromatebtn"):
                        
                    st.session_state["selected_reagents"].append("acidified potassium dichromate")
                    st.rerun()
                
            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_darkblue.svg",width=30)
                st.caption("Oxalic Acid",text_alignment="center")
                if st.button("Added ✅" if "oxalic acid" in st.session_state["selected_reagents"] else "Add",
                            disabled= "oxalic acid" in st.session_state["selected_reagents"],
                            key = "oxalic_acid_btn"):
                    
                    st.session_state["selected_reagents"].append("oxalic acid")
                    st.rerun()   

            with st.container(border=True,horizontal_alignment="center",gap="xxsmall"):
                st.image("images/reagents/bottle_yellow.svg",width=30)
                st.caption("Conc. H₂SO₄",text_alignment="center")
                if st.button("Added ✅" if "concentrated sulphuric acid" in st.session_state["selected_reagents"] else "Add",
                            disabled= "concentrated sulphuric acid" in st.session_state["selected_reagents"],
                            key = "conc_h2so4__btn"):
                    
                    st.session_state["selected_reagents"].append("concentrated sulphuric acid")
                    st.rerun() 

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
    st.title("WHAT DOES IT THIS SUGGEST?", text_alignment="center")
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

def feedback_screen(feedback_type = "feedback"): 
    #default anion - just for safety
    # feedback type can be "feedback" or "feedback_cation"
    st.title("FEEDBACK", text_alignment="center")
    st.divider()
    st.error("Incorrect guess!")
    st.subheader("Would you like feedback?")
    with st.container(horizontal=True,horizontal_alignment="center",gap="medium"):
        msg = ""
        if st.button("Yes - Show Feedback!",width="stretch"):
            msg, st.session_state["curr_state"] = logic.handle_action(feedback_type, "yes")
        if st.button("No - End Phase",width="stretch",type="primary"):
            msg, st.session_state["curr_state"] = logic.handle_action(feedback_type, "no")
        
    st.warning(msg)

def main():
    if st.session_state["curr_state"] == "start":
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
        feedback_screen("feedback")
    elif st.session_state["curr_state"] == "feedback_cation":
        feedback_screen("feedback_cation")

main()

