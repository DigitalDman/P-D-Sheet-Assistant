## P&D Sheet Assistant ##
import time
import webbrowser
import random
from Pokemon import *
from Digimon import *

import sys
import os
import json

# Dynamically find the folder where the .exe resides
exe_dir = os.path.dirname(sys.executable)
exe_dir = exe_dir + "\\_internal" ## If your exporting the exe. Comment out for IDE Testing

digimon_file_path = os.path.join(exe_dir, "digimon_sheets.json")
pokemon_file_path = os.path.join(exe_dir, "pokemon_sheets.json")

pokemon_list = []
digimon_list = []
character_used = None
new_character_created = False

###### SAVE & LOAD #####
def save():
    global exe_dir, digimon_file_path, pokemon_file_path

    ### Lets save the Digimon data first ###
    digimon_save_data = []

    for digimon in digimon_list:
        digimon_save_data.append( digimon.save_list() ) ## Save EVERYTHING to digimon_save_data

    with open(digimon_file_path, "w", encoding="utf-8") as digimon_file: ## Opens/Creates the digimon_sheets.json file, encodes it for Python to interpret
        #print(digimon_save_data)
        json.dump(digimon_save_data, digimon_file) ## Saves it as a JSON to preserve it as a list
        
    ### Lets save the Pokemon data next ###
    pokemon_save_data = []

    for pokemon in pokemon_list:
        pokemon_save_data.append( pokemon.save_list() ) ## Save EVERYTHING to pokemon_save_data

    with open(pokemon_file_path, "w", encoding="utf-8") as pokemon_file: ## Opens/Creates the pokemon_sheets.json file, encodes it for Python to interpret
        #print(pokemon_save_data)
        json.dump(pokemon_save_data, pokemon_file) ## Saves it as a JSON to preserve it as a list



def load():
    global exe_dir, digimon_file_path, pokemon_file_path, digimon_list, pokemon_list

    try:
        ### Lets load the Digimon data
        digimon_data = []
        with open(digimon_file_path, "r", encoding="utf-8") as digimon_file:
            digimon_data = json.load(digimon_file)

        #print(digimon_data)
        for digimon in digimon_data:
            new_digimon = Digimon("New")
            new_digimon.load(digimon)
            digimon_list.append( new_digimon )

        #print(digimon_list)

        ### Now to load the pokemon ###
        pokemon_data = []
        with open(pokemon_file_path, "r", encoding="utf-8") as pokemon_file:
            pokemon_data = json.load(pokemon_file)

        for pokemon in pokemon_data:
            new_pokemon = Pokemon("NEW")
            new_pokemon.load(pokemon)
            digimon_list.append
    except Exception:
        pass

    
    


########################

def clear_terminal():
    # \033[2J clears the screen, \033[H moves the cursor to the top-left corner
    print("\033[H\033[2J", end="")######### CLEAR TERMINAL FUNCTION #########


def do_you_accept_changes(): #returns boolean, TRUE if the user accepts changes and FALSE if the user does not accept changes


    inputAssured = True


    while inputAssured:
        try:
            user = str(input("Do you accept these changes? (y/n) "))


            if user.lower() == "y" or user.lower() == "n":
                inputAssured = False
       
        except Exception:
            print("Invalid input. Enter a letter. (y/n) ", end="")
            inputAssured = True
   
    if user == "y":
        return True
    else:
        return False


def press_enter_to_continue():
    input("Press Enter to Continue")
    clear_terminal()


#############################################

def remove_character(character_type):
    global character_used, new_character_created
    clear_terminal()
    selection = 0
    #characters_displayed = 1

    ## Doing a Try...Except to assure input
    while True:

        characters_displayed = 1

        print(f"Please Select your character, or create a new sheet")
        if character_type == "Digimon":
            for i in digimon_list:
                print(f"\t{characters_displayed}. {i.name}")
                characters_displayed += 1

            print("--------------------------------------------")
            print (f"\t{characters_displayed}. Exit ")
        ##### Pokemons #######
        elif character_type == "Pokemon":
            for i in pokemon_list:
                print(f"\t{characters_displayed}. {i.name}")
                characters_displayed += 1
            print("--------------------------------------------")
            print (f"\t{characters_displayed}. Exit")

        #################
        try:
            selection = int(input("Selection: "))
            
            if (selection < 1 or selection > characters_displayed):
                print(5/0) ## Trigger the catch
            
            break


        except Exception:
            ### When an error is triggered. Print the error message & Clear the terminal
            clear_terminal()
            print(f"ERROR. Selection made is out of range. Please enter a number from 1-{characters_displayed}.")
            time.sleep(1)
            clear_terminal()

    if selection == characters_displayed:
        return
    else:
        clear_terminal()

        character_selected = None

        if character_type == "Digimon":
            character_selected = digimon_list[selection - 1]
        else:
            character_selected = pokemon_list[selection - 1]

        print(f"{character_selected.name} will be deleted")
        
        if do_you_accept_changes():
            if character_type == "Digimon":
                digimon_list.pop(selection - 1)
            else:
                pokemon_list.pop(selection - 1)



def select_character(character_type):
    global character_used, new_character_created
    clear_terminal()
    selection = 0

    ## Doing a Try...Except to assure input
    while True:

        characters_displayed = 1

        print(f"Please Select your character, or create a new sheet")
        if character_type == "Digimon":
            for i in digimon_list:
                print(f"\t{characters_displayed}. {i.name}")
                characters_displayed += 1

            print("--------------------------------------------")
            print (f"\t{characters_displayed}. New Rookie")
        ##### Pokemons #######
        elif character_type == "Pokemon":
            for i in pokemon_list:
                print(f"\t{characters_displayed}. {i.name}")
                characters_displayed += 1
            print("--------------------------------------------")
            print (f"\t{characters_displayed}. New Base Form")

        print (f"\t{characters_displayed + 1}. Switch character type")
        print (f"\t{characters_displayed + 2}. Delete character")
        #################
        try:
            selection = int(input("Selection: "))
            
            if (selection < 1 or selection > characters_displayed + 2):
                print(5/0) ## Trigger the catch
            
            break


        except Exception:
            ### When an error is triggered. Print the error message & Clear the terminal
            clear_terminal()
            print(f"ERROR. Selection made is out of range. Please enter a number from 1-{characters_displayed + 2}.")
            time.sleep(1)
            clear_terminal()

    ##### Create a new character #######
    if selection == characters_displayed:
        new_character_created = True

        if character_type == "Digimon":
            character_name = input("Enter the Digimon's name: ") ## Get the characters name
            print("Opening Genai's Notes...")

            new_digimon = Digimon(character_name) ## Create the character object
            #print(new_digimon)
            digimon_list.append( new_digimon ) ## Save it to our list
            character_used = digimon_list[ digimon_list.index(new_digimon) ] ## Select our character
            #print(character_used)

            time.sleep(0.5)
    
            webbrowser.open("https://digimon.fandom.com/wiki/"+character_name) ## Open the Pokemons Pokedex page


            

        if character_type == "Pokemon": ### Do the same stuff as above
            character_name = input("Enter the Pokemon's name: ") ## Get the characters name
            print("Opening Pokedex...")

            new_pokemon = Pokemon(character_name)
            pokemon_list.append( new_pokemon )
            character_used = pokemon_list[ pokemon_list.index(new_pokemon) ]

            time.sleep(0.5)
    
            webbrowser.open("https://pokemondb.net/pokedex/"+character_name) ## Open the Pokemons Pokedex page

    elif selection == characters_displayed + 1:
        clear_terminal()
        return False

    elif selection == characters_displayed + 2:
        clear_terminal()
        remove_character(character_type)
        select_character(character_type)
        
    else:
        #### Select an existing character ######
        if character_type == "Digimon":
            character_used = digimon_list[selection - 1]
            print("Opening Genai's Notes...")
            time.sleep(0.5)
            webbrowser.open("https://digimon.fandom.com/wiki/"+ character_used.name) ## Open the Pokemons Pokedex page

        else:
            character_used = pokemon_list[selection - 1]
            print("Opening Pokedex...")
            time.sleep(0.5)
            webbrowser.open("https://pokemondb.net/pokedex/"+ character_used.name) ## Open the Pokemons Pokedex page

    return True
    clear_terminal()




######### DEFINE CHARACTER TYPE METHOD #########
def declare_character_type():
    selection = 0


   # print("Selection: ")


    ## Doing a Try...Except to assure input
    while True:


        #print(f"{selected_menu}")
        print("What type of character are you working with?")
        print("\t1.Digimon")
        print("\t2.Pokemon")


        try:
            selection = int(input("Selection: "))
           
            if (selection < 1 or selection > 2):
                print(5/0) ## Trigger the catch
           
            break


        except Exception:
            ### When an error is triggered. Print the error message & Clear the terminal
            clear_terminal()
            print("ERROR. Selection made is out of range. Please enter a number from 1-2.")
            time.sleep(1)
            clear_terminal()
       
   
    match selection:
        case 1:
            if select_character("Digimon") == False:
                declare_character_type()
            else:
                return "Digimon"
        case 2:
            if select_character("Pokemon") == False:
                declare_character_type()
            else:
                return "Pokemon"



######################################################


######### GENERATE POKEMON STATS #########
def generate_pokemon_stats(character):
    clear_terminal()
    selection = 0
    dice_20 = ""

    '''
    selection = ""

    while (selection != "y" and selection != "n"):
        print("Would you like to randomly generate the remaining stats? (y/n)", end="")
        selection = input()
   
    if selection == "n":
        return
    else:
        print("generating remaining stats...")


        ## Randomly generate the remaining stats
        dice = ["D12", "D10", "D8", "D6", "D4"]
        stats = ["Fight", "Flight", "Brawn", "Brains", "Charm", "Grit"]
        stats.remove(dice_20) ## Remove the D20 stat from this list


        for i in range(dice):
            stat_selected = random.choice(stats)
            stats.remove(stat_selected)
            print(f"{i} {stat_selected}")
        '''




######################################################


######### BUILD A SHEET #########
def build_a_sheet(character_type, build = False): ## Setting a default value makes it an option peramiter
    global character_used
    ## Variables ##
    character_name = ""

    clear_terminal()


    #### Run this if the characters a Pokemon ####
    if character_type == "Pokemon":
        #character_name = input("Enter the Pokemon's name: ") ## Get the characters name
        #print("Opening Pokedex...")
        #time.sleep(1)




        #webbrowser.open("https://pokemondb.net/pokedex/"+character_name) ## Open the Pokemons Pokedex page

        #test_pokemon = Pokemon("Eevee")
        #test_pokemon.determine_hp()
        #test_pokemon.evolution()
        #test_pokemon.determine_move()
        ### And Pokemon Creation Submenu
        #clear_terminal()
       


        ## Doing a Try...Except to assure input
        while True:

            if build:
                print(f"Creating the character sheet for {character_used.name}")
            else:
                print(f"Modifying character sheet for {character_used.name}")
            
            print("\t1. Calculate Lvl 1 HP")
            print("\t2. Find D20")
            print("\t3. Select Stats")
            print("\t4. Add +1's")
            print("\t5. Select Stage")

            if build:
                print("\t6.Finish Creating Sheet")
            else:
                print("\t6.Return to main menu")


            try:
                selection = int(input("Selection: "))
            
                if (selection < 1 or selection > 6):
                    print(5/0) ## Trigger the catch
            
                break


            except Exception:
                ### When an error is triggered. Print the error message & Clear the terminal
                clear_terminal()
                print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                time.sleep(1)
                clear_terminal()
        
        clear_terminal()
        match selection:
            case 1: ## Calculate HP
                character_used.determine_hp() ## Figure out the HP of the used character
                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 2: ## Find the Pokemon's D20
                character_used.find_D20()
                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 3: ## Change the pokemon's stats
                character_used.change_stats()
                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 4: ## Add +1's
                while True:
                    try:
                        print(f"How many +1's would you like to add to {character_used.name}?")
                        modifiers_added = int(input("Selection: "))

                        if modifiers_added < 1:
                            print(5/0)

                        new_modifiers = character_used.plus_ones(modifiers_added)

                        clear_terminal()
                        #### Print the new modifiers
                        print("\nNew Modifiers")
                        for key in new_modifiers:
                            print(f"{key} - {new_modifiers[key]}")

                        if do_you_accept_changes():
                            print("Changes made")
                            character_used.modifiers = new_modifiers
                        else:
                            print("Aborting Changes")

                        break
                    except Exception:
                        print("Error. Please input a valid number")

                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 5: ## Select Pokemon Stage
                character_used.select_stage()
                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 6: ## Return to main menu
                return
                    
    else:
        ## Doing a Try...Except to assure input
        while True:

            if build:
                print(f"Creating the character sheet for {character_used.name}")
            else:
                print(f"Modifying character sheet for {character_used.name}")
            
            print("\t1. Calculate Lvl 1 HP")
            print("\t2. Select Stats")
            print("\t3. Add +1's")
            print("\t4. Select Stage")

            if build:
                print("\t5.Finish Creating Sheet")
            else:
                print("\t5.Return to main menu")


            try:
                selection = int(input("Selection: "))
            
                if (selection < 1 or selection > 5):
                    print(5/0) ## Trigger the catch
            
                break


            except Exception:
                ### When an error is triggered. Print the error message & Clear the terminal
                clear_terminal()
                print("ERROR. Selection made is out of range. Please enter a number from 1-5.")
                time.sleep(1)
                clear_terminal()
        
    
        match selection:
            case 1: ## Calculate HP
                clear_terminal()
                character_used.calculate_health() ## Figure out the HP of the used character
                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 2: ## Change the Digimon's stats
                clear_terminal()
                character_used.change_stats()
                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 3: ## Add +1's
                clear_terminal()
                while True:
                    try:
                        print(f"How many +1's would you like to add to {character_used.name}?")
                        modifiers_added = int(input("Selection: "))

                        if modifiers_added < 1:
                            print(5/0)

                        new_modifiers = character_used.plus_ones(modifiers_added)

                        clear_terminal()
                        #### Print the new modifiers
                        print("\nNew Modifiers")
                        for key in new_modifiers:
                            print(f"{key} - {new_modifiers[key]}")

                        if do_you_accept_changes():
                            print("Changes made")
                            character_used.modifiers = new_modifiers
                        else:
                            print("Aborting Changes")

                        break
                    except Exception:
                        print("Error. Please input a valid number")

                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 4: ## Select Digimon Stage
                clear_terminal()
                character_used.select_stage()
                press_enter_to_continue()
                save()
                build_a_sheet(character_type)

            case 5: ## Return to main menu
                return      
                        



               


######### MAIN MENU #########
def main_menu(start = False):
    global character_used
    clear_terminal()
    selection = 0
    character_type = ""


   # print("Selection: ")

    if start:
        character_type = declare_character_type()
        clear_terminal()

        if new_character_created:
            build_a_sheet(character_type, new_character_created)
            clear_terminal()


    ## Doing a Try...Except to assure input
    while True:

        print(f"Welcome to the P&D Sheet Assistant. What would you like to do?")
        print(f"Selected Character - {character_used.name}")
        print("\t1. Modify a Sheet")
        print(f"\t2. Level up {character_used.name}")
        print("\t3. Digivolve/Evolve")
        print("\t4. Display Sheet Information")
        print("\t5. Change selected character")
        print("\t6. Save & Exit Program")


        try:
            selection = int(input("Selection: "))
           
            if (selection < 1 or selection > 6):
                print(5/0) ## Trigger the catch
           
            break


        except Exception:
            ### When an error is triggered. Print the error message & Clear the terminal
            clear_terminal()
            print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
            time.sleep(1)
            clear_terminal()
   
    #### Call the declare character type with the proper submenu ####
    clear_terminal()
    ############ UNFINISHED ##########################
    match selection:
        case 1:
            build_a_sheet(character_type, False)
            save()

            main_menu()

        case 2:
            
            if character_type == "Pokemon":
                character_used.pokemon_level_up()
            else:
                character_used.level_up()

            press_enter_to_continue()
            save()

            main_menu()

        case 3:
            if character_type == "Pokemon":
                character_used.evolve()
            else:
                character_used.digivolve()

            press_enter_to_continue()
            save()

            main_menu()

        case 4:
            print("Current Sheet Information")
            print("-----------------------------------------------------------------------------------------------------------")
            character_used.proper_display()
            print("-----------------------------------------------------------------------------------------------------------")
            press_enter_to_continue()
            save()

            main_menu()
        
        case 5:
            main_menu(True) ## Recursion Loop back



load()
main_menu(True)
save()

time.sleep(25)

#print(digimon_file_path)
#print(pokemon_file_path)