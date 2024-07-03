from dice import Dice
from house import House
from playerinteractions import PlayerInteraction


class Player():
    def __init__(self, name : str, house : House = None, playerinteraction: PlayerInteraction=None, dice : Dice=None):
        self.name = name
        self.house = house
        self.type = playerinteraction
        self.choose_dice = dice
    def __repr__(self):
        pass

    def choose_dice(self):
        pass

    def choose_action(self):
        pass

    def save(self):
        pass

    def load(self):
        pass