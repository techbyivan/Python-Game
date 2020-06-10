class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=10, mopiness=10):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.discipline = discipline
        self.hunger = hunger
        self.mopiness = mopiness

    def get_name(self):
        self.name = ""

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    
    def get_disciplined(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

grayson = Pet("Grayson")
grayson.eat_food()
print(grayson.fullness)
# 80
print(grayson.happiness)
# 50

boog = Pet("Boog")
boog.get_love()
print(grayson.fullness)
# 50
print(boog.happiness)
# 80