import random

#global variables
user_dry_guess = None
user_confirmatory_guess = None


anions = ("acetate",
           "carbonate", "sulphide", "sulphite", "nitrite",
           "chloride", "bromide", "iodide", "nitrate",
           "sulphate")
ion_type = "anion"
ion = random.choice(anions)
anion_data = {
            #acetate test
            "acetate":{
                "dry_test":{
                    "action": ("oxalic acid", "water drops"),
                    "observation": "vinegar smell"
                },
                "confirmatory_test":{
                    "action": ("water", "ferric chloride"),
                    "observation": "reddish-brown color"
                }
            },
            #dil hcl test
            "carbonate":{
                "dry_test":{
                    "action": ("dilute hydrochloric acid",),
                    "observation": "brisk effervescence"
                },
                "confirmatory_test":{
                    "action": ("water","magnesium sulphate"),
                    "observation": "milky white precipitate"
                }
            },

            "sulphide":{
                "dry_test":{
                    "action": ("dilute hydrochloric acid",),
                    "observation": "rotten egg smell"
                },
                "confirmatory_test":{
                    "action": ("water","lead acetate"),
                    "observation": "black precipitate"
                }
            },

            "sulphite":{
                "dry_test":{
                    "action": ("dilute hydrochloric acid",),
                    "observation": "burning sulphur smell"
                },
                "confirmatory_test":{
                    "action": ("water","acidified potassium dichromate"),
                    "observation": "green color"
                }
            },
            
            "nitrite":{
                "dry_test":{
                    "action": ("dilute hydrochloric acid",),
                    "observation": "brown fumes"
                },
                "confirmatory_test":{
                    "action": ("water","oxalic acid","ferrous sulphate"),
                    "observation": "red color"
                }
            },

            #conc hcl test
            "chloride":{
                "dry_test":{
                    "action": ("concentrated hydrochloric acid","heat"),
                    "observation": "white fumes"
                },
                "confirmatory_test":{
                    "action": ("water","silver nitrate"),
                    "observation": "white precipitate"
                }
            },

            "bromide":{
                "dry_test":{
                    "action": ("concentrated hydrochloric acid","heat"),
                    "observation": "brown fumes"
                },
                "confirmatory_test":{
                    "action": ("water","silver nitrate"),
                    "observation": "pale yellow precipitate"
                }
            },

            "iodide":{
                "dry_test":{
                    "action": ("concentrated hydrochloric acid","heat"),
                    "observation": "violet fumes"
                },
                "confirmatory_test":{
                    "action": ("water","silver nitrate"),
                    "observation": "yellow precipitate"
                }
            },

            "nitrate":{
                "dry_test":{
                    "action": ("concentrated sulphuric acid","copper turnings","heat"),
                    "observation": "brown fumes"
                },
                "confirmatory_test":{ #brown ring test
                    "action": ("water","ferrous sulphate","concentrated sulphuric acid"),
                    "observation": "brown ring at the junction of two liquids"
                }
            },

            #no dry test for sulphate, only confirmatory test
            "sulphate":{
                "dry_test":{
                    "action": (), #it has no dry test
                    "observation": "no reaction"
                },
                "confirmatory_test":{
                    "action": ("water","barium chloride"),
                    "observation": "white precipitate"
                }  
            }
}

def test_evaluator(ion_type, ion, test_type, user_action):
    #Compare action and return observation if action is correct else return no reaction

    # ion_type: "anion" or "cation"
    # ion: name of the ion to be gussed
    # test_type: "dry_test" or "confirmatory_test"
    # user_action: (tuple) of actions performed by the user in the test 

    ref_data = None
    if ion_type == "anion":
        ref_data = anion_data[ion][test_type]
    else:
        # cation test data to be added later
        pass

    if sorted(user_action) == sorted(ref_data["action"]):
        return ref_data["observation"]
    else:
        return "no reaction"
    
#print(test_evaluator("anion", "acetate", "dry_test", ("water drops", "oxalic acid")))

def user_console(ion):
    #This function will handle the user interaction
    print("Perfom dry test")
    curr_state = "awaiting_dry_test"
    while curr_state != "done":
        if curr_state == "awaiting_dry_test":
            user_dry_action = user_action_input()
            dry_test_result, curr_state = handle_action(curr_state, user_dry_action)
            print(dry_test_result)
        elif curr_state == "interpreting_dry_test":
            user_dry_guess = input("Which anion maybe present? ")
            msg, curr_state = handle_action(curr_state, user_dry_guess)
            print(msg)
        elif curr_state == "awaiting_confirmatory_test":
            user_confirmatory_action = user_action_input()
            confirmatory_test_result, curr_state = handle_action(curr_state, user_confirmatory_action)
            print(confirmatory_test_result)
        elif curr_state == "interpreting_confirmatory_test":
            user_confirmatory_guess = input("Which anion is present and confirmed? ")
            msg, curr_state = handle_action(curr_state, user_confirmatory_guess)
            print(msg)
        elif curr_state == "feedback":
            user_wants_feedback = input("Do you want feedback/suggestions? (yes/no) ")
            msg, curr_state = handle_action(curr_state, user_wants_feedback,confirmatory_test_result)
            print(msg)
    print("Test complete. Thank you for playing!")

def user_action_input():

    user_action = input("Enter actions performed (comma separated): ").split(",")
    user_action = tuple([action.strip() for action in user_action])
    return user_action

def handle_action(state, user_input,confirmatory_test_result=None):
    global user_dry_guess , user_confirmatory_guess
    if state == "awaiting_dry_test":
        # Process dry test action
        result = test_evaluator(ion_type, ion, "dry_test", user_input)
        if result != "no reaction":
            return result, "interpreting_dry_test" #next state
        else:
            return result, "awaiting_dry_test" #next state = current state, ask for input again
        
    elif state == "interpreting_dry_test":
        # Process dry test results and determine next steps
        user_dry_guess = user_input
        return "Move to confirmatory test", "awaiting_confirmatory_test" #next state

    elif state == "awaiting_confirmatory_test":
        # Process confirmatory test action
        result = test_evaluator(ion_type, ion, "confirmatory_test", user_input)
        if result != "no reaction":
            return result, "interpreting_confirmatory_test" #next state
        else:
            return result, "feedback"

    elif state == "interpreting_confirmatory_test":
        # Process confirmatory test results and determine final outcome
        user_confirmatory_guess = user_input
        if user_confirmatory_guess == ion:
            return "Correct! The ion is present.", "done"
        else:
            return "Incorrect guess!", "feedback"
    elif state == "feedback":
        #will provide a feedback only if the user wants
        if user_input == "yes":
            if user_dry_guess == ion:
                if user_confirmatory_guess != ion: 
                    return "Did you guess the ion after confirmatory test correctly?", "interpreting_confirmatory_test"
                elif confirmatory_test_result == "no reaction":
                    return "Did you perform the correct confirmatory test?", "awaiting_confirmatory_test"
                
            else: #dry test guess or action was wrong
                return "Did you perform the dry test correctly?", "awaiting_dry_test"
        else:
            return f"No feedback/sugesstion provided. The ion was {ion}", "done"
            
    elif state == "done":
        return "Thank you for playing!", "done"



user_console(ion)



