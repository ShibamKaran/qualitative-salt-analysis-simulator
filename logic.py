import random

#global variables
anion_dry_guess = None
anion_confirmatory_guess = None
cation_wet_guess = None
cation_confirmatory_guess = None

anion_complete = False
cation_complete = False

#anions and their test data
anions = ("acetate",
           "carbonate", "sulphide", "sulphite", "nitrite",
           "chloride", "bromide", "iodide", "nitrate",
           "sulphate")
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
                    "action": ("concentrated hydrochloric acid","copper turnings","heat"),
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

#cations and their test data
cations = ("ammonium",
            "lead", "copper",
            "ferric", "aluminium",
            "zinc", "cobalt", "nickel", "manganese",
            "barium", "calcium", "strontium", 
            "magnesium")

cation_data = {
            #group 0
            "ammonium":{
                "wet_test":{
                    "action": ("concentrated sodium hydroxide", "heat"),
                    "observation": "ammonia smell"
                },
                "confirmatory_test":{
                    "action": ("concentrated sodium hydroxide", "heat","nessler's reagent"),
                    "observation": "brown precipitate"
                }
            },
            #group 1
            "lead":{
                "wet_test":{
                    "action": ("water","dilute hydrochloric acid"),
                    "observation": "white precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","potassium iodide"),
                    "observation": "yellow precipitate"
                }
            },
            #group 2
            "copper":{
                "wet_test":{
                    "action": ("water","dilute hydrochloric acid","sodium sulphide"),
                    "observation": "black precipitate"
                },
                "confirmatory_test":{ 
                    "action": ("water","ammonium hydroxide"),
                    "observation": "deep blue color"
                }
            },
            #group 3
            "ferric":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide"),
                    "observation": "reddish-brown precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","dilute hydrochloric acid","potassium ferrocyanide"),
                    "observation": "prussian blue color"
                }
            },
            "aluminium":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide"),
                    "observation": "white precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","dilute hydrochloric acid","blue litmus solution", "ammonium hydroxide"),
                    "observation": "suspended blue precipitate"
                }
            },
            #group 4
            "zinc":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "sodium sulphide"),
                    "observation": "white precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","potassium ferrocyanide"),
                    "observation": "bluish-white precipitate"
                }
            },
            "cobalt":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "sodium sulphide"),
                    "observation": "black precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","potassium nitrite", "ammonium hydroxide"),
                    "observation": "yellow precipitate"
                }
            },
            "nickel":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "sodium sulphide"),
                    "observation": "black precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","sodium hydroxide", "bromine water"),
                    "observation": "black precipitate"
                }
            },
            "manganese":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "sodium sulphide"),
                    "observation": "flesh-colored precipitate"
                },
                "confirmatory_test":{
                    "action": ("water", "sodium hydroxide"),
                    "observation": "white precipitate"
                }
            },
            #group 5
            "barium":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "ammonium carbonate"),
                    "observation": "white precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","potassium chromate"),
                    "observation": "yellow precipitate"
                }
            },
            "calcium":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "ammonium carbonate"),
                    "observation": "white precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","ammonium oxalate"),
                    "observation": "white precipitate"
                }
            },
            "strontium":{
                "wet_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "ammonium carbonate"),
                    "observation": "white precipitate"
                },
                "confirmatory_test":{
                    "action": ("water","ammonium sulphate"),
                    "observation": "white precipitate" 
                }
            },
            #group 6
            "magnesium":{
                "wet_test":{
                    "action": (),
                    "observation": "no reaction"
                },
                "confirmatory_test":{
                    "action": ("water","ammonium chloride","ammonium hydroxide", "diammonium hydrogen phosphate"),
                    "observation": "white precipitate"
                }
            }
}           

anion = random.choice(anions)
cation = random.choice(cations)

def test_evaluator(ion_type, ion, test_type, user_action):
    #Compare action and return observation if action is correct else return no reaction

    # ion_type: "anion" or "cation"
    # ion: name of the ion to be gussed
    # test_type: anions - "dry_test" or "confirmatory_test"
    #            cations - "wet_test" or "confirmatory_test"
    # user_action: (tuple) of actions performed by the user in the test 

    ref_data = None
    if ion_type == "anion":
        ref_data = anion_data[ion][test_type] 
    else: #cation
        ref_data = cation_data[ion][test_type]

    if sorted(user_action) == sorted(ref_data["action"]):
        return ref_data["observation"]
    else:
        return "no reaction"
    
#print(test_evaluator("anion", "acetate", "dry_test", ("water drops", "oxalic acid")))

def handle_action(state, user_input,confirmatory_test_result=None):
    #state function
    #states: 
    # anions-
    #   "awaiting_dry_test", "interpreting_dry_test", "awaiting_confirmatory_test", "interpreting_confirmatory_test", "feedback"
    # cations-
    #   "awaiting_wet_test", "interpreting_wet_test", "awaiting_confirmatory_test_cation", "interpreting_confirmatory_test_cation", "feedback_cation"
    # choosing phase - symbolic state
    global anion_dry_guess , anion_confirmatory_guess , cation_wet_guess , cation_confirmatory_guess, anion_complete, cation_complete
        
    if state == "awaiting_dry_test":
        # Process dry test action
        result = test_evaluator("anion", anion, "dry_test", user_input)
        return result, "interpreting_dry_test" #next state
        
    elif state == "interpreting_dry_test":
        # Process dry test results and determine next steps
        anion_dry_guess = user_input
        if anion_dry_guess == "cannot guess yet":
            return "Let's do another dry test!", "awaiting_dry_test" #stay in the same state
        else:
            return "Move to confirmatory test", "awaiting_confirmatory_test" #next state

    elif state == "awaiting_confirmatory_test":
        # Process confirmatory test action
        result = test_evaluator("anion", anion, "confirmatory_test", user_input)
        if result != "no reaction":
            return result, "interpreting_confirmatory_test" #next state
        else:
            return result, "feedback"

    elif state == "interpreting_confirmatory_test":
        # Process confirmatory test results and determine final outcome
        anion_confirmatory_guess = user_input
        if anion_confirmatory_guess == anion:
            anion_complete = True
            return "Correct! The ion is present.", "choosing_phase"
        else:
            return "Incorrect guess!", "feedback"
    elif state == "feedback":
        #will provide a feedback only if the user wants
        if user_input == "yes":
            if anion_dry_guess == anion:
                if anion_confirmatory_guess != anion and confirmatory_test_result != "no reaction": 
                    return "Did you guess the ion after confirmatory test correctly?", "interpreting_confirmatory_test"
                else: #confirmatory_test_result == "no reaction":
                    return "Did you perform the correct confirmatory test?", "awaiting_confirmatory_test"
                
            else: #dry test guess or action was wrong
                return "Did you perform the dry test correctly?", "awaiting_dry_test"
        else:
            anion_complete = True
            return f"No feedback/sugesstion provided. The anion was {anion}", "choosing_phase"

    elif state == "awaiting_wet_test":
        # process wet test action
        result = test_evaluator("cation", cation, "wet_test", user_input)
        return result, "interpreting_wet_test" #next state
        
    elif state == "interpreting_wet_test":
        # process wet test results and determine next steps
        cation_wet_guess = user_input
        if cation_wet_guess == ("cannot guess yet",):
            return "Let's do another wet test!", "awaiting_wet_test" #stay in the same state
        else:
            return "Move to confirmatory test", "awaiting_confirmatory_test_cation" #next state        

    elif state == "awaiting_confirmatory_test_cation":
        # process confirmatory test action for cation and determine next steps
        result = test_evaluator("cation", cation, "confirmatory_test", user_input)
        return result, "interpreting_confirmatory_test_cation" #next state
        
    elif state == "interpreting_confirmatory_test_cation":
        # process confirmatory test results for cation and determine final outcome
        cation_confirmatory_guess = user_input
        if cation_confirmatory_guess == "cannot guess yet":
            return "Let's do another confirmatory test!", "awaiting_confirmatory_test_cation" #stay in the same state
        elif cation_confirmatory_guess == cation:
            cation_complete = True
            return "Correct! The ion is present.", "choosing_phase"
        else:
            return "Incorrect guess!", "feedback_cation"
        
    elif state == "feedback_cation":
        #will provide a feedback only if the user wants
        if user_input == "yes":
            if cation in cation_wet_guess:
                if cation_confirmatory_guess != cation and confirmatory_test_result != "no reaction":
                    return "Did you guess the ion after confirmatory test correctly?", "interpreting_confirmatory_test_cation"
                else: #confirmatory_test_result == "no reaction":
                    return "Did you perform the correct confirmatory test?", "awaiting_confirmatory_test_cation"
            else: #wet test guess or action was wrong
                return "Did you perform the wet test correctly?", "awaiting_wet_test"
        else:
            cation_complete = True             
            return f"No feedback/sugesstion provided. The cation was {cation}", "choosing_phase"
