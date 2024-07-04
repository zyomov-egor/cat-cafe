from random import randint
from random import choice

from house_new import House

items = [1, 2, 3, 4, 5, 6]
class AI():
    def choose_dice(self, lst_dices: list=None):
        """выбирает произвоьный кубик из трех или двух в зависимости от хода, i_player = True если игрок выбирает кубик первым"""
        return choice(lst_dices)

    def choose_action(self, house: House=None, dices=(int, int)):
        tower = randint(1,5)
        if tower % 2 == 1:
            if (house[12 - 2 * dices[0]][dices[1] - 1] != "NAN") and (house[12 - 2 * dices[0]][dices[1] - 1] not in items):
                return (tower, dices[0], dices[1])
            elif (house[12 - 2 * dices[1]][dices[0] - 1] != "NAN") and (house[12 - 2 * dices[1]][dices[0] - 1] not in items):
                return (tower, dices[1], dices[0])
            else:
                return None
        else:
            if (house[13 - 2 * dices[0]][dices[1] - 1] != "NAN") and (house[13 - 2 * dices[0]][dices[1] - 1] not in items):
                return (tower, dices[0], dices[1])
            elif (house[13 - 2 * dices[1]][dices[0] - 1] != "NAN") and (house[13 - 2 * dices[1]][dices[0] - 1] not in items):
                return (tower, dices[1], dices[0])
            else:
                return None

