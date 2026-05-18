import streamlit as st
import logic

#session states i.e. global variable
if "anion_complete" not in st.session_state:
    st.session_state["anion_complete"] = False

if "cation_complete" not in st.session_state:
    st.session_state["cation_complete"] = False

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
        start = st.button("Start Practice",
                on_click=phase_selection_screen,
                )
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
    st.space("large")
    with st.container(horizontal=True, horizontal_alignment="center"):
        if st.session_state.anion_complete:
            st.success("**Anion — Acid Radical**  \n\n:small[Dry test + Confirmatory test]   \n\n**✓ Complete**")
        elif not st.session_state["anion_complete"]:
            with st.container(horizontal_alignment='center',border=True):
                st.markdown("**Anion — Acid Radical**  \n\n:small[Dry test + Confirmatory test]")
                st.button("Start Anion Analysis", width="stretch")

        if st.session_state["cation_complete"]:
            st.success("**Cation — Basic Radical**  \n\n:small[Wet test + Confirmatory test]  \n\n**✓ Complete**")
        elif not st.session_state["cation_complete"]:
            with st.container(horizontal_alignment='center',border=True):
                st.markdown("**Cation — Basic Radical**  \n\n:small[Wet test + Confirmatory test]")
                st.button("Start Cation Analysis", width="stretch")

def anion_dry_test_screen():
    pass

def main():
    if st.session_state["curr_state"] == "start":
        start_screen()
    elif st.session_state["curr_state"] == "choosing_phase":
        phase_selection_screen()

main()