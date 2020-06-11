class Toy:
    def __init__(self, bonus=10, newness=10, cuteness='Yes'):
        self.bonus = 10
        self.newness = 10
        self.cuteness = 10

    def use(self):
        if self.newness == 0:
            return 0
        else:
            self.newness -= 1
            return self.bonus

    def purchase(self):
        if self.cuteness == "Yes":
            return "Awwwww...I have to get this"
        else:
            return "No Worries....Maybe next time"