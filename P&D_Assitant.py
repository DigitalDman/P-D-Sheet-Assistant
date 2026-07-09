## P&D Sheet Assitant ##
import time
import webbrowser
import random

######### CLEAR TERMINAL FUNCTION #########
def clear_terminal():
    # \033[2J clears the screen, \033[H moves the cursor to the top-left corner
    print("\033[H\033[2J", end="")


#############################################


######### DEFINE CHARACTER TYPE METHOD #########
def declare_character_type(selected_menu):
    selection = 0

   # print("Selection: ")

    ## Doing a Try...Except to assure input
    while True:

        print(f"{selected_menu}")
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
            return "Digimon"
        case 2:
            return "Pokemon"


######################################################

######### GENERATE POKEMON STATS #########
def generate_pokemon_stats(character):
    clear_terminal()
    selection = 0
    dice_20 = ""

    ### Assure Input
    while True:

        print(f"What is {character}'s highest base stat")
        print("\t1. Attack")
        print("\t2. Defense")
        print("\t3. Sp. Attack")
        print("\t4. Sp. Defense")
        print("\t5. Speed")

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
        case 1:
            print(f"{character}'s D20 is Fight")
            dice_20 = "Fight"
        case 2:
            print(f"{character}'s D20 is Brawn")
            dice_20 = "Brawn"
        case 3:
            print(f"{character}'s D20 is Brains")
            dice_20 = "Brains"
        case 4:
            print(f"{character}'s D20 is Grit")
            dice_20 = "Grit"
        case 5:
            print(f"{character}'s D20 is Flight")
            dice_20 = "Flight"
    
    print("--------------------------------------------------")
    time.sleep(1)

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


######################################################

######### BUILD A SHEET #########
def build_a_sheet():
    ## Variables ##
    character_name = ""


    clear_terminal()
    character_type = declare_character_type("Build A Sheet")
    clear_terminal()

    #### Run this if the characters a Pokemon ####
    if character_type == "Pokemon":
        character_name = input("Enter the Pokemon's name: ") ## Get the characters name
        print("Opening Pokedex...")
        time.sleep(1)


        webbrowser.open("https://pokemondb.net/pokedex/"+character_name) ## Open the Pokemons Pokedex page

        ### And Pokemon Creation Submenu
        clear_terminal()
        

    ## Doing a Try...Except to assure input
    while True:

        print("What would you help with?")
        print("\t1.Calculate HP")
        print("\t2.Find D20 & Generate Stage 1 Stats")
        print("\t3.Return to main menu")

        try:
            selection = int(input("Selection: "))
            
            if (selection < 1 or selection > 3):
                print(5/0) ## Trigger the catch
            
            break

        except Exception:
            ### When an error is triggered. Print the error message & Clear the terminal
            clear_terminal()
            print("ERROR. Selection made is out of range. Please enter a number from 1-3.")
            time.sleep(1)
            clear_terminal()
        
    
    match selection:
        case 1:
            return
        case 2:
            generate_pokemon_stats(character_name)

                
        



######### MAIN MENU #########
def main_menu():
    clear_terminal()
    selection = 0

   # print("Selection: ")

    ## Doing a Try...Except to assure input
    while True:

        print(f"Welcome to the P&D Sheet Assitant. What would you like to do?")
        print("What type of character are you working with?")
        print("\t1.Build a Sheet")
        print("\t2.Level up an existing Sheet")
        print("\t3.Digivolve/Evolve")

        try:
            selection = int(input("Selection: "))
            
            if (selection < 1 or selection > 3):
                print(5/0) ## Trigger the catch
            
            break

        except Exception:
            ### When an error is triggered. Print the error message & Clear the terminal
            clear_terminal()
            print("ERROR. Selection made is out of range. Please enter a number from 1-3.")
            time.sleep(1)
            clear_terminal()
    
    #### Call the declare character type with the proper submenu ####
    
    ############ UNFINISHED ##########################
    match selection:
        case 1:
            build_a_sheet()


main_menu()