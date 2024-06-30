import json
from random import randint
SIDES = [1, 2, 3, 4, 5, 6]
class Dice():
    def __init__(self):
        self.current_side = SIDES[randint(0, 5)]

    def __repr__(self):
        return str(self.side)

    def roll(self):
        self.current_side = SIDES[randint(0, 5)]

    def save(self):
        with open('data1.json', 'w') as file:
            json.dump({"current_side":self.current_side}, file)
            return {"current_side":self.current_side}

    @staticmethod
    def load():
        with open('data1.json', 'r') as file:
            s = json.load(file)
        return s["current_side"]
