from random import randint
class Dice():
    def __init__(self):
        self.sides = [1, 2, 3, 4, 5, 6]
        self.side = self.sides[randint(0, 5)]

    def __repr__(self):
        return str(self.side)

    def roll(self):
        return Dice()

    def save(self):
        pass

    def load(self):
        pass

c1 = Dice()
c2 = Dice()
c3 = Dice()
print(c1, c1.roll())

