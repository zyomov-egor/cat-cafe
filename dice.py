from random import randint
class Dice():
    def __init__(self):
        dices = [1, 2, 3, 4, 5, 6]
        self.dice = dices[randint(0, 5)]
    def __repr__(self):
        return str(self.dice)
