from logic import *
import logic

def tuple_input(msg):

    inp = input(msg).split(",")
    inp = tuple([action.lower().strip() for action in inp])
    return inp

def user_console_anion():
    #this function will handle the anion part user interaction
    #every variable in this func is a local var, update to global variable takes place in handle_action func
    print("Perfom dry test")
    curr_state = "awaiting_dry_test"
    action_input_msg = "Enter actions performed (comma separated): "
    while curr_state != "choosing_phase":
        if curr_state == "awaiting_dry_test":
            user_dry_action = tuple_input(action_input_msg)
            dry_test_result, curr_state = handle_action(curr_state, user_dry_action)
            print(dry_test_result)
        elif curr_state == "interpreting_dry_test":
            anion_dry_guess = input("Which anion maybe present? ").lower().strip()
            msg, curr_state = handle_action(curr_state, anion_dry_guess)
            print(msg)
        elif curr_state == "awaiting_confirmatory_test":
            user_confirmatory_action = tuple_input("Enter actions performed (comma separated): ")
            confirmatory_test_result, curr_state = handle_action(curr_state, user_confirmatory_action)
            print(confirmatory_test_result)
        elif curr_state == "interpreting_confirmatory_test":
            anion_confirmatory_guess = input("Which anion is present and confirmed? ").lower().strip()
            msg, curr_state = handle_action(curr_state, anion_confirmatory_guess)
            print(msg)
        elif curr_state == "feedback":
            user_wants_feedback = input("Do you want feedback/suggestions? (yes/no) ").lower().strip()
            msg, curr_state = handle_action(curr_state, user_wants_feedback,confirmatory_test_result)
            print(msg)
    print("Anion test complete. Thank you for playing!")

def user_console_cation():
    #this function will handle the cation part user interaction
    #every variable in this func is a local var, update to global variable takes place in handle_action func
    print("Perfom wet test")
    curr_state = "awaiting_wet_test"
    action_input_msg = "Enter actions performed (comma separated): "
    
    while curr_state != "choosing_phase":
        if curr_state == "awaiting_wet_test":
            user_wet_action = tuple_input(action_input_msg)
            wet_test_result, curr_state = handle_action(curr_state, user_wet_action)
            print(wet_test_result)
        elif curr_state == "interpreting_wet_test":
            cation_wet_guess = tuple_input("Which cations maybe present?(comma separated) ")
            msg, curr_state = handle_action(curr_state, cation_wet_guess)
            print(msg)
        elif curr_state == "awaiting_confirmatory_test_cation":
            user_confirmatory_action = tuple_input(action_input_msg)
            confirmatory_test_result, curr_state = handle_action(curr_state, user_confirmatory_action)
            print(confirmatory_test_result)
        elif curr_state == "interpreting_confirmatory_test_cation":
            cation_confirmatory_guess = input("Which cation is present and confirmed? ").lower().strip()
            msg, curr_state = handle_action(curr_state, cation_confirmatory_guess)
            print(msg)
        elif curr_state == "feedback_cation":
            user_wants_feedback = input("Do you want feedback/suggestions? (yes/no) ").lower().strip()
            msg, curr_state = handle_action(curr_state, user_wants_feedback,confirmatory_test_result)
            print(msg)
    print("Cation test complete. Thank you for playing!")

def user_console():
    #this function will handle the overall user interaction for both anion and cation testing
    while not(logic.anion_complete and logic.cation_complete):
        phase = input("Do you want to test for anions or cations? (anion/cation) ").lower().strip()
        if phase == "anion":
            user_console_anion()
        elif phase == "cation":
            user_console_cation()
    
    print("All tests complete. Thank you for playing!")
    print(f"The salt was {logic.cation} {logic.anion}")

user_console()