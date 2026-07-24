import time

class Pokemon:


    ### Storing attributes ###
    name = ""
    stats = {
        "Fight" : "",
        "Flight" : "",
        "Brawn" : "",
        "Brains" : "",
        "Charm" : "",
        "Grit" : "",
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
    stage = 1
    hp = 1

    ### Constructor ###
    def __init__(self, name):
        self.name = name

    def clear_terminal(self):
        # \033[2J clears the screen, \033[H moves the cursor to the top-left corner
        print("\033[H\033[2J", end="")######### CLEAR TERMINAL FUNCTION #########

   

    def load(self, name, stats, level, stage):
        self.name = name
        self.stats = stats
        self.level = level
        self.stage = stage
   
    def test_display(self):
        print(self.name)
        print(self.stats)
        print(self.level)
        print(self.stage)

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

    def determine_hp(self): #returns base HP

        inputAssured = True
        while inputAssured:
            try:
                user = int(input(f"What is the base HP of {self.name}? "))
                inputAssured = False

            except Exception:
                print("Invalid input. Enter a number. ")
                inputAssured = True

        self.blinking_text("Calculating HP", "Calculated")
                
        base = user/10 + 1/4

        print(f"The determined HP is: {base}")

        if self.do_you_accept_changes():
            return base
        else: 
            return -1

    def evolution(self):
      
        ### Digivolution Blinking thingy ###
        self.clear_terminal()
        print("E")
        time.sleep(0.1)
        self.clear_terminal()
        print("")
        self.clear_terminal()
        time.sleep(0.1)


        print("E")
        time.sleep(0.1)
        self.clear_terminal()
        print("")
        self.clear_terminal()
        time.sleep(0.1)


        print("E")
        time.sleep(0.1)
        self.clear_terminal()
        print("")
        self.clear_terminal()
        time.sleep(0.1)
       
        print("E")
        time.sleep(0.1)
        self.clear_terminal()
        print("Ev")
        time.sleep(0.1)
        self.clear_terminal()
        print("Evo")
        time.sleep(0.1)
        self.clear_terminal()
        print("Evol")
        time.sleep(0.3)
        self.clear_terminal()
        print("Evolu")
        time.sleep(0.1)
        self.clear_terminal()
        print("Evolut")
        time.sleep(0.1)
        self.clear_terminal()
        print("Evoluti")
        time.sleep(0.1)
        self.clear_terminal()
        print("Evolutio")
        time.sleep(0.1)
        self.clear_terminal()
        print("Evolution")
        time.sleep(0.1)
        self.clear_terminal()

    ###########################################
        time.sleep(1)

    def extra_damage(self):
        inputAssured = True
       
        while inputAssured:
            try:
                user = int(input(f"1. Normal Pokemon\n2. Special Pokemon\nSelect 1 or 2: "))
                inputAssured = False

                if user > 2 or user < 1:
                    print("Enter 1 or 2")
                    inputAssured = True
            except Exception:
                "Invalid input. Enter 1 or 2."
                inputAssured = True
               
        inputAssured = True

        if user == 1:

            print(f"\t1. Base")
            print(f"\t2. Stage 1")
            print(f"\t3. Stage 2")

            while inputAssured:
                try:
                    stage = int(input(f"Select the stage: "))
                    inputAssured = False

                    if stage > 3 or stage < 1:
                        print("Invalid input. Select a number (1-3).")
                        inputAssured = True

                except Exception:
                    print("Invalid input. Select a number (1-3).")
                    inputAssured = True

            if stage == 1:
                damage_bonus = 0
           
            elif stage == 2:
                damage_bonus = 1
            
            else:
                damage_bonus = 2
           
        inputAssured = True
           
        if user == 2:
            
            print(f"\t1. Mystical/Mega")
            print(f"\t2. Legendary")
            print(f"\t3. Legendary Mega")
           
            while inputAssured:
                
                try:
                    stage = int(input(f"Select the stage: "))
                    inputAssured = False

                    if stage > 3 or stage < 1:
                        print("Invalid input. Select a number (1-3).")
                        inputAssured = True

                except Exception:
                    print("Invalid input. Select a number (1-3).")
                    inputAssured = True

            if stage == 1:
                damage_bonus = 3
           
            elif stage == 2:
                damage_bonus = 4

            else:
                damage_bonus = 5   
            
        if self.do_you_accept_changes():
            return damage_bonus
        else:
            return -1   

    def determine_move(self):

        inputAssured = True

        while inputAssured:
            try:
                user = int(input(f"1. Normal Pokemon\n2. Special Pokemon\nSelect 1 or 2: "))
                inputAssured = False

                if user > 2 or user < 1:
                    print("Enter 1 or 2. ")
                    inputAssured = True
                
            except Exception:
                print("Invalid input. Enter 1 or 2.")
                inputAssured = True

        inputAssured = True

        if user == 1: #if the user chooses a normal pokemon

            while inputAssured:
                brain_dice = str(input("What brain dice do you possess? "))
                if brain_dice.lower() == "d4":
                    inputAssured = False
                    moves = 5
                elif brain_dice.lower() == "d6":
                    inputAssured = False 
                    moves = 6
                elif brain_dice.lower() == "d8":
                    inputAssured = False
                    moves = 7
                elif brain_dice.lower() == "d10":
                    inputAssured = False
                    moves = 8
                elif brain_dice.lower() == "d12":
                    inputAssured = False
                    moves = 9
                elif brain_dice.lower() == "d20":
                    inputAssured = False
                    moves = 10
                else:
                    print("Invalid input. Try again")
                    inputAssured = True


        else: #if the user chooses a special pokemon
            moves = 20
            
        if self.do_you_accept_changes():
            return moves
        else:
            return -1
        
    def pokemon_level_up(self):
        inputAssured = True
            
        while inputAssured:
            try:
                user = int(input(f"1.\tNormal Pokemon\n2.\tMythical Pokemon\n3.\tLegendary\n Selection(1-3): "))
                inputAssured = False
            
                if user > 3 or user < 1:
                    print("Out of range. Selection (1-3).")
                    inputAssured = True
                    
            except Exception:
                print("Invalid input. Try again. ")
                inputAssured = True
                
        inputAssured = True
                   
        if user == 1: #if the user chooses 1 (Normal Pokemon)
            
            while inputAssured:
                try:
                    level_increase = int(input(f"Normal Pokemon: Maximum - 20\nHow many times do you want to level up? "))
                    inputAssured = False
                    
                    if level_increase < 1 or level_increase > 20 - self.level:
                        print("Please input a valid number.")
                        inputAssured = True

                except Exception:
                    print("Please enter a valid number.")
                    inputAssured = True
                    
            
            if not self.stats["Brawn"]: #checks to see if the string is empty 
                while True:
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
                                self.stats["Brawn"] ="D20"
                            case 2:
                                self.stats["Brawn"] = "D12"
                            case 3:
                                self.stats["Brawn"] = "D10"
                            case 4:
                                self.stats["Brawn"] = "D8"
                            case 5:
                                self.stats["Brawn"] = "D6"
                            case 6:
                                self.stats["Brawn"] = "D4"
                       
                        break

                    except Exception:
                        ### When an error is triggered. Print the error message & Clear the terminal
                        self.clear_terminal()
                        print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                        time.sleep(1)
                        self.clear_terminal()

            
            for i in range(level_increase):
                brawn_dice_string = self.stats["Brawn"]
                brawn_dice_string = brawn_dice_string.replace("D","")
                brawn_dice = int(brawn_dice_string)
            
                hp += brawn_dice//4   
                
            
            plus_1s_gained = ( (self.level + level_increase) // 3 ) - ( self.level // 3 )
            self.blinking_text("Checking for +1's gained", f"{plus_1s_gained} +1's are gained")
            time.sleep(1)
            self.clear_terminal()
            new_modifiers = self.plus_ones(plus_1s_gained) ## Gain the +1’s
            time.sleep(1)
            self.clear_terminal()
            
            extra_damage_gained = ( (self.level + level_increase) // 4 ) - ( self.level // 4 )
            self.blinking_text("Checking for extra damage gained", f"{extra_damage_gained} extra damage gained")
            self.clear_terminal()  
            
            print("Changes made")
            print(f"New HP Stat: {hp}")
            print("\nNew Modifiers")
            for key in new_modifiers:
                print(f"{key} - {new_modifiers[key]}")

            print(f"New Extra Damage - +{self.extra_damage + extra_damage_gained}")
            print("")
            
            if self.do_you_accept_changes():
                self.clear_terminal()
                self.blinking_text("Making changes", "Changes made")


                self.level = self.level + level_increase
                self.modifiers = new_modifiers
                self.extra_damage += extra_damage_gained
                self.hp = hp
                time.sleep(1)
                
            else:
                self.blinking_text("Aborting Changes", "Aborting Changes")

                
        elif user == 2: #if the user chooses 2 (Mythical Pokemon)
            
            while inputAssured:
                try:
                    level_increase = int(input(f"Mythical Pokemon: Maximum - 30\nHow many times do you want to level up? "))
                    inputAssured = False
                    
                    if level_increase < 1 or level_increase > 30 - self.level:
                        print("Please input a valid number.")
                        inputAssured = True

                except Exception:
                    print("Please enter a valid number.")
                    inputAssured = True

            if not self.stats["Brawn"]: #checks to see if the string is empty 
                while True:
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
                                self.stats["Brawn"] ="D20"
                            case 2:
                                self.stats["Brawn"] = "D12"
                            case 3:
                                self.stats["Brawn"] = "D10"
                            case 4:
                                self.stats["Brawn"] = "D8"
                            case 5:
                                self.stats["Brawn"] = "D6"
                            case 6:
                                self.stats["Brawn"] = "D4"
                       
                        break

                    except Exception:
                        ### When an error is triggered. Print the error message & Clear the terminal
                        self.clear_terminal()
                        print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                        time.sleep(1)
                        self.clear_terminal()

            
            for i in range(level_increase):
                brawn_dice_string = self.stats["Brawn"]
                brawn_dice_string = brawn_dice_string.replace("D","")
                brawn_dice = int(brawn_dice_string)
            
                hp += brawn_dice//4   
                
            
            plus_1s_gained = ( (self.level + level_increase) // 3 ) - ( self.level // 3 )
            self.blinking_text("Checking for +1's gained", f"{plus_1s_gained} +1's are gained")
            time.sleep(1)
            self.clear_terminal()
            new_modifiers = self.plus_ones(plus_1s_gained) ## Gain the +1’s
            time.sleep(1)
            self.clear_terminal()
            
            extra_damage_gained = ( (self.level + level_increase) // 4 ) - ( self.level // 4 )
            self.blinking_text("Checking for extra damage gained", f"{extra_damage_gained} extra damage gained")
            self.clear_terminal()  
            
            print("Changes made")
            print(f"New HP Stat: {hp}")
            print("\nNew Modifiers")
            for key in new_modifiers:
                print(f"{key} - {new_modifiers[key]}")

            print(f"New Extra Damage - +{self.extra_damage + extra_damage_gained}")
            print("")
            
            if self.do_you_accept_changes():
                self.clear_terminal()
                self.blinking_text("Making changes", "Changes made")


                self.level = self.level + level_increase
                self.modifiers = new_modifiers
                self.extra_damage += extra_damage_gained
                self.hp = hp
                time.sleep(1)
                
            else:
                self.blinking_text("Aborting Changes", "Aborting Changes")
                
                
        else: #if the user chooses 3
            while inputAssured:
                try:
                    level_increase = int(input(f"Legendary Pokemon: Maximum - 40\nHow many times do you want to level up? "))
                    inputAssured = False
                    
                    if level_increase < 1 or level_increase > 40 - self.level:
                        print("Please input a valid number.")
                        inputAssured = True

                except Exception:
                    print("Please enter a valid number.")
                    inputAssured = True
                    
            if not self.stats["Brawn"]: #checks to see if the string is empty 
                while True:
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
                                self.stats["Brawn"] ="D20"
                            case 2:
                                self.stats["Brawn"] = "D12"
                            case 3:
                                self.stats["Brawn"] = "D10"
                            case 4:
                                self.stats["Brawn"] = "D8"
                            case 5:
                                self.stats["Brawn"] = "D6"
                            case 6:
                                self.stats["Brawn"] = "D4"
                       
                        break

                    except Exception:
                        ### When an error is triggered. Print the error message & Clear the terminal
                        self.clear_terminal()
                        print("ERROR. Selection made is out of range. Please enter a number from 1-6.")
                        time.sleep(1)
                        self.clear_terminal()

            
            for i in range(level_increase):
                brawn_dice_string = self.stats["Brawn"]
                brawn_dice_string = brawn_dice_string.replace("D","")
                brawn_dice = int(brawn_dice_string)
            
                hp += brawn_dice//4   
                
            
            plus_1s_gained = ( (self.level + level_increase) // 3 ) - ( self.level // 3 )
            self.blinking_text("Checking for +1's gained", f"{plus_1s_gained} +1's are gained")
            time.sleep(1)
            self.clear_terminal()
            new_modifiers = self.plus_ones(plus_1s_gained) ## Gain the +1’s
            time.sleep(1)
            self.clear_terminal()
            
            extra_damage_gained = ( (self.level + level_increase) // 4 ) - ( self.level // 4 )
            self.blinking_text("Checking for extra damage gained", f"{extra_damage_gained} extra damage gained")
            self.clear_terminal()  
            
            print("Changes made")
            print(f"New HP Stat: {hp}")
            print("\nNew Modifiers")
            for key in new_modifiers:
                print(f"{key} - {new_modifiers[key]}")

            print(f"New Extra Damage - +{self.extra_damage + extra_damage_gained}")
            print("")
            
            if self.do_you_accept_changes():
                self.clear_terminal()
                self.blinking_text("Making changes", "Changes made")


                self.level = self.level + level_increase
                self.modifiers = new_modifiers
                self.extra_damage += extra_damage_gained
                self.hp = hp
                time.sleep(1)
                
            else:
                self.blinking_text("Aborting Changes", "Aborting Changes")


 





    
            






          



        
                