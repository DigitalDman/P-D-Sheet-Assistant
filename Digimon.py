import time

class Digimon:

    ### Storing attributes ###
    name = ""
    stats = {
        "Fight" : "D4",
        "Flight" : "D4",
        "Brawn" : "D20",
        "Brains" : "D4",
        "Charm" : "D4",
        "Grit" : "D4",
    } ## Close dictionary

    modifiers = {
        "Fight" : 0,
        "Flight" : 0,
        "Brawn" : 0,
        "Brains" : 0,
        "Charm" : 0,
        "Grit" : 0,
    } ## Close dictionary

    level = 1
    hp = 0


    stage_index = 2
    stage = ["Fresh", "In-Training", "Rookie", "Champion", "Ultimate", "Mega"] ## Digimon stages go as follows ##
    ## Fresh -> In-Training -> Rookie -> Champion -> Ultimate -> Mega ##

    ### Constructor ###
    def __init__(self, name):
        self.name = name

    
    def clear_terminal(self):
        # \033[2J clears the screen, \033[H moves the cursor to the top-left corner
        print("\033[H\033[2J", end="")
    

    def do_you_accept_changes(self): #returns boolean, TRUE if the user accepts changes and FALSE if the user does not accept changes
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


    def load(self, name, stats, level, stage): ## Load some of the stuff (gotta add or rewrite some of this load stuff)
        self.name = name
        self.stats = stats
        self.level = level
        #self.stage = stage


    def test_display(self): ## display all our variables for a test
        print(self.name)
        print(self.stats)
        print(self.hp)
        print(self.modifiers)
        print(self.level)
        print(self.stage[self.stage_index])


    def increase_health(self, digivolve):
        
        if self.stats["Brawn"] == "" or self.digivolve:

            while True: ### Loop to get what the D20 is
                if digivolve:
                    print(f"What is {self.name}'s next forms Brawn?")
                else:
                    print(f"What is {self.name}'s brawn dice?")

                print("\t1. D20")
                print("\t2. D12")
                print("\t3. D10")
                print("\t4. D8")
                print("\t5. D6")
                print("\t6. D4")


                try:
                    selection = int(input("Selection: "))
                    
                    if (selection < 1 or selection > 6):
                        print(5/0) ## Trigger the catch
                    
                    match selection: ## Save the value of the D20 as an int
                        case 1:
                            brawn_dice = 20
                        case 2:
                            brawn_dice = 12
                        case 3:
                            brawn_dice = 10
                        case 4:
                            brawn_dice = 8
                        case 5:
                            brawn_dice = 6
                        case 6:
                            brawn_dice = 4

                    break

                except Exception:
                    ### When an error is triggered. Print the error message & Clear the terminal
                    self.clear_terminal()
                    print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                    time.sleep(1)
                    self.clear_terminal()
        else:
            ## Save the value of the dice without the D infront of it
            brawn_dice_string = self.stats["Brawn"]
            brawn_dice_string = brawn_dice_string.replace("D","")
            brawn_dice = int(brawn_dice_string)

        inputAssured = True

        while inputAssured:
            try:
                user = str(input(f"Does {self.name} have the ability Fighting Spirit? (y/n) "))


                if user.lower() == "y" or user.lower() == "n":
                    inputAssured = False
        
            except Exception:
                print("Invalid input. Enter a letter. (y/n) ", end="")
                inputAssured = True
    
        if user == "y":
            new_hp_stat = self.hp + brawn_dice // 2 ## Floor divide
        else:
            new_hp_stat = self.hp + brawn_dice // 4 ## Floor divide

        

        print(f"{self.name}'s new HP would be {new_hp_stat}") ## Print what the new hp would be

        return new_hp_stat


    def plus_ones(self, modifiers_gained):

        new_modifiers = self.modifiers

        print(f"{self.name} also gains {modifiers_gained} +1's") ## Now lets get our +1's



        for i in range(modifiers_gained): ## Because we have to do this twice
             while True: ### Loop to get what the D20 is
                print(f"Which stat you you want +1 # {i + 1} in?")
                print("\t1. Fight")
                print("\t2. Flight")
                print("\t3. Brawn")
                print("\t4. Brains")
                print("\t5. Charm")
                print("\t6. Grit")


                try:
                    selection = int(input("Selection: "))
                    
                    if (selection < 1 or selection > 6):
                        print(5/0) ## Trigger the catch
                    
                    match selection:
                        case 1:
                            new_modifiers["Fight"] += 1
                        case 2:
                            new_modifiers["Flight"] += 1
                        case 3:
                            new_modifiers["Brawn"] += 1
                        case 4:
                            new_modifiers["Brains"] += 1
                        case 5:
                            new_modifiers["Charm"] += 1
                        case 6:
                            new_modifiers["Grit"] += 1
                    
                    self.clear_terminal()

                    break

                except Exception:
                    ### When an error is triggered. Print the error message & Clear the terminal
                    self.clear_terminal()
                    print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                    time.sleep(1)
                    self.clear_terminal()    
        
        return new_modifiers


    def blinking_text(self, blink_text, final_text): # I dont know how to describe this with comments
        ## Its kinda just a ... loading thingy?
        self.clear_terminal()
        print(f"{blink_text}")
        time.sleep(0.5)
        self.clear_terminal()
        print(f"{blink_text}.")
        time.sleep(0.5)
        self.clear_terminal()
        print(f"{blink_text}..")
        time.sleep(0.5)
        self.clear_terminal()
        print(f"{blink_text}...")
        time.sleep(0.5)
        self.clear_terminal()

        self.clear_terminal()
        print(f"{blink_text}")
        time.sleep(0.5)
        self.clear_terminal()
        print(f"{blink_text}.")
        time.sleep(0.5)
        self.clear_terminal()
        print(f"{blink_text}..")
        time.sleep(0.5)
        self.clear_terminal()
        print(f"{blink_text}...")
        time.sleep(0.5)
        self.clear_terminal()

        print(f"{final_text}")


    def increase_dice(self, dice):
        match dice:
            case "D12":
                return "D20"
            case "D10":
                return "D12"
            case "D8":
                return "D10"
            case "D6":
                return "D8"
            case "D4":
                return "D6"


    def select_stat(self):

        while True: ### Loop to get what the D20 is
            print("What would you like to change this dice to?")
            print(f"\t1. D20")
            print(f"\t2. D12")
            print(f"\t3. D10")
            print(f"\t4. D8")
            print(f"\t5. D6")
            print(f"\t6. D4")


            try:
                selection = int(input("Selection: "))
                
                if (selection < 1 or selection > 6):
                    print(5/0) ## Trigger the catch
                
                match selection:
                    case 1:
                        return "D20"
                    case 2:
                        return "D12"
                    case 3:
                        return "D10"
                    case 4:
                        return "D8"
                    case 5:
                        return "D6"
                    case 6:
                        return "D4"
                        

                break

            except Exception:
                ### When an error is triggered. Print the error message & Clear the terminal
                self.clear_terminal()
                print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                time.sleep(1)
                self.clear_terminal()


    def select_stage(self):
        new_stage = ""

        while True:
            print(f"What stage is {self.name}")
            print(f"\t1. Rookie")
            print(f"\t2. Champion")
            print(f"\t3. Ultimate")
            print(f"\t4. Mega")

            try:
                selection = int(input("Selection: "))
                
                if (selection < 1 or selection > 4):
                    print(5/0) ## Trigger the catch
                
                self.clear_terminal()
                match selection:
                    case 1:
                        new_stage = "Rookie"
                    case 2:
                        new_stage = "Champion"
                    case 3:
                        new_stage = "Ultimate"
                    case 4:
                        new_stage = "Mega"
                break

            except Exception:
                ### When an error is triggered. Print the error message & Clear the terminal
                self.clear_terminal()
                print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                time.sleep(1)
                self.clear_terminal()
        
        self.clear_terminal()
        print("Changes Made")
        print(f"Stage - {new_stage}")
        print("")

        if self.do_you_accept_changes():
            self.stage = new_stage


    def change_stats(self):
        continue_changing_stats = True
        new_stats = self.stats

        while continue_changing_stats:

            while True:
                print("What stats would you like to change?")
                print(f"\t1. Fight - {self.stats["Fight"]}")
                print(f"\t2. Flight - {self.stats["Flight"]}")
                print(f"\t3. Brawn - {self.stats["Brawn"]}")
                print(f"\t4. Brains - {self.stats["Brains"]}")
                print(f"\t5. Charm - {self.stats["Charm"]}")
                print(f"\t6. Grit - {self.stats["Grit"]}")


                try:
                    selection = int(input("Selection: "))
                    
                    if (selection < 1 or selection > 6):
                        print(5/0) ## Trigger the catch
                    
                    self.clear_terminal()
                    match selection:
                        case 1:
                            new_stats["Fight"] = self.select_stat()
                        case 2:
                            new_stats["Flight"] = self.select_stat()
                        case 3:
                            new_stats["Brawn"] = self.select_stat()
                        case 4:
                            new_stats["Brains"] = self.select_stat()
                        case 5:
                            new_stats["Charm"] = self.select_stat()
                        case 6:
                            new_stats["Grit"] = self.select_stat()


                    break

                except Exception:
                    ### When an error is triggered. Print the error message & Clear the terminal
                    self.clear_terminal()
                    print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                    time.sleep(1)
                    self.clear_terminal()
                
            self.clear_terminal()

            print("Changes Made")
            print("\nNew Stats")
            for key in new_stats:
                print(f"{key} - {new_stats[key]}")


            print("")

            if self.do_you_accept_changes(): ## If you accept the changes then save everything (and Digivolve!)
                self.stats = new_stats
                self.blinking_text("Changing stats", "Stats Changed")
            
            ###### Check if you want to continue
            inputAssured = True

            while inputAssured:
                try:
                    user = str(input("Do you want to continue making changes to your stats? (y/n) "))


                    if user.lower() == "y" or user.lower() == "n":
                        inputAssured = False
            
                except Exception:
                    print("Invalid input. Enter a letter. (y/n) ", end="")
                    inputAssured = True
        
            if user == "y":
                continue_changing_stats = True
            else:
                print("Leaving stat change submenu")
                time.sleep(1)
                continue_changing_stats = False


    def digivolve(self):
        new_stats = self.stats

        ### Digivolution Blinking thingy ###
        self.clear_terminal()
        print("D")
        time.sleep(0.1)
        self.clear_terminal()
        print("")
        self.clear_terminal()
        time.sleep(0.1)

        print("D")
        time.sleep(0.1)
        self.clear_terminal()
        print("")
        self.clear_terminal()
        time.sleep(0.1)

        print("D")
        time.sleep(0.1)
        self.clear_terminal()
        print("")
        self.clear_terminal()
        time.sleep(0.1)
        
        print("D")
        time.sleep(0.1)
        self.clear_terminal()
        print("Di")
        time.sleep(0.1)
        self.clear_terminal()
        print("Dig")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digi")
        time.sleep(0.3)
        self.clear_terminal()
        print("Digiv")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digivo")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digivol")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digivolu")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digivolut")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digivoluti")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digivolutio")
        time.sleep(0.1)
        self.clear_terminal()
        print("Digivolution")
        time.sleep(0.1)
        self.clear_terminal()

        ###########################################
        time.sleep(1)

        new_hp_stat = self.increase_health(True) ## Can increase health method
        
        print(f"{self.name} might also gain a flaw, be sure to check that on your character sheet!") ## Nothing to be done on the code end of this, just a reminder for whovers using this to Digivolve
        time.sleep(2)
        self.clear_terminal()

        #print("\n")
        ##### +1's #########
        
        new_modifiers = self.plus_ones(2) ## Call the plus ones method, two plus ones are gained

        ##### Stage goes up ########
        new_stage_index = self.stage_index + 1

        #### Increase a dice value by 1 ####

        while True: ### Loop to get what Dice you want to increase
                print(f"Which stat would you like to increase by a dice value")
                
                line_count = 1
                line_indexs = []
                for i in self.stats:
                    if self.stats[i] != "D20":
                        print(f"\t{line_count}. {i} - {self.stats[i]}")
                        line_indexs.append(i)
                        line_count += 1


                try:
                    selection = int(input("Selection: "))
                    #print(selection)
                    #print(line_count - 1)
                    
                    if (selection < 1 or selection > line_count - 1):
                        print(5/0) ## Trigger the catch
                    
                    selection -= 1 ## So we can call it in the line_indexs array easier
                    new_stats[ line_indexs[selection] ] = self.increase_dice( self.stats[ line_indexs[selection] ] )
                    
                    self.clear_terminal()

                    break

                except Exception:
                    ### When an error is triggered. Print the error message & Clear the terminal
                    #self.clear_terminal()
                    print(f"ERROR. Selection made is out of range. Please enter a number from 1-{line_count - 1}.")
                    time.sleep(1)
                    self.clear_terminal()    

        ###### Confirm Changes ########
        self.clear_terminal() ## Confirm what changes are made
        print("Changes made")
        print(f"New HP Stat: {new_hp_stat}")
        print(f"New Stage: {self.stage[new_stage_index]}")

        print("\nNew Modifiers")
        for key in new_modifiers:
            print(f"{key} - {new_modifiers[key]}")
        
        print("\nNew Stats")
        for key in new_stats:
            print(f"{key} - {new_stats[key]}")


        print("")

        if self.do_you_accept_changes(): ## If you accept the changes then save everything (and Digivolve!)
            self.hp = new_hp_stat
            self.modifiers = new_modifiers
            self.stage_index = new_stage_index
            self.stats = new_stats

            new_character_name = input("Enter the new forms name: ") ## Get the characters name
            
            self.blinking_text(f"{self.name} Digivolve to", f"{new_character_name}")
            self.name = new_character_name

