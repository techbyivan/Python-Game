class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=10, mopiness=10):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []

    def get_name(self):
        self.name = ""

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    
    def give_timeout(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

    def get_toy(self, toy):
        self.toys.append(toy)
    
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)


class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        
    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()






