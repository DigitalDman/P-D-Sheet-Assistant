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

    level = 1
    stage = 1

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
                user = int(input(f"1. Normal Pokemon\n2. Special Pokemon"))
                inputAssured = False

                if user > 2 or user < 1:
                    print("Enter 1 or 2")
                    inputAssured = True

            except Exception:
                print("Invalid input. Enter 1 or 2.")
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
                    inputAssurd = True

            if stage == 1:
                return 0
            
            elif stage == 2:
                return 1

            else:
                return 2
            
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
                    inputAssurd = True

            if stage == 1:
                return 3
            
            elif stage == 2:
                return 4

            else:
                return 5   

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
                    return 5
                elif brain_dice.lower() == "d6":
                    inputAssured = False 
                    return 6
                elif brain_dice.lower() == "d8":
                    inputAssured = False
                    return 7
                elif brain_dice.lower() == "d10":
                    inputAssured = False
                    return 8
                elif brain_dice.lower() == "d12":
                    inputAssured = False
                    return 9
                elif brain_dice.lower() == "d20":
                    inputAssured = False
                    return 10
                else:
                    print("Invalid input. Try again")
                    inputAssured = True


        else: #if the user chooses a special pokemon
            return 20
 





    
            






          



        
                