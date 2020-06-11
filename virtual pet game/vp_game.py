class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=10, mopiness=10):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def get_name(self):
        self.name = ""

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    
    def give_timeout(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
    
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)

boogie = Pet("Boogie", 70, 5, 80, 90)





