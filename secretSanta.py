import random

if __name__ == "__main__":

    # list of people and their partners
    # if no partner, value will be ""
    partner_dict = {
        "Adrian": "Ally",
        "Ally": "Adrian",
        "Tristan": "Kat",
        "Kat": "Tristan",
        "Dave": "Tori",
        "Tori": "Dave",
        "Michael": "Melanie",
        "Melanie": "Michael"
    }

    # List of keys 
    names = [name for name in partner_dict.keys() if name != ""]

    # Change to true when matches are complete
    good_matches = False
    while (not good_matches):  # main loop
        random.seed()  # new seed
        name_list = names[:]  # fresh copy of name_list

        # set up matches dict
        matches_dict = {name: "" for name in name_list}
        matches_dict["Dave"] = "Adrian"  # already picked a present!

        # will contain list of givers that already have chosen their receiver
        already_chosen = []

        # remove all pre-arranged choices
        for giver, receiver in matches_dict.items():
            try:
                name_list.remove(receiver)
                already_chosen.append(giver)
            except:
                pass

        # start creating matches
        for giver in matches_dict.keys():
            if giver not in already_chosen:
                fail_out = False  # set true when no good choices are left
                good_choice = False  # set to true when giver assigned valid receiver
                
                # Loops until valid choice made or no valid choice
                while (not good_choice):
                    receiver = random.choice(name_list)  # get random receiver from remaining names
                    # verify rules
                    if partner_dict[giver] != receiver and giver != receiver and matches_dict[receiver] != giver:
                        good_choice = True  # exit while loop
                        name_list.remove(receiver)
                        matches_dict[giver] = receiver
                    else:
                        fail_out = True  # default to no valid choice
                        # ensure the giver has a valid receiver
                        for remaining_person in name_list:
                            if partner_dict[giver] != remaining_person and giver != remaining_person and matches_dict[remaining_person] != giver:
                                fail_out = False  
                        if fail_out:
                            break  # break out of loop, no valid choices
                if fail_out:
                    break  # break out of loop, matches will not be valid
        
        # if no fail_out, matches are complete
        if not fail_out:
            good_matches = True
                    
    print("GIVER\t\tRECEIVER")
    for giver, receiver in matches_dict.items():
        print("{}\t\t{}".format(giver, receiver))
