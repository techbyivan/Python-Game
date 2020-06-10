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
    
    def get_timeout(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

grayson = Pet("Grayson")
grayson.eat_food()

print("Grayson's Fullness: " + str(grayson.fullness))
print("Grayson's Happiness: "+ str(grayson.happiness))

boog = Pet("Boog")
boog.get_love()

print("Boog's Fullness: " + str(boog.fullness))
print("Boog's Happiness: "+ str(boog.happiness))

class HappyPet(Pet):
    pass