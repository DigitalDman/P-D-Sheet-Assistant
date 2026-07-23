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

    def determine_hp():

        inputAssured = True
        while inputAssured:
            try:
                user = int(input("What is the base HP of {self.name}? "))
                inputAssured = False

            except Exception:
                print("Invalid input. Enter a number. ")
                inputAssured = True
        
        base = user/10 + 1/4

        return base
                