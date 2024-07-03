from dice import Dice
from house_new import House
from player import Player


def test_init():
    p = Player(name='George', house=House(), dice=Dice())
    assert p.name == 'George'
    assert p.tower_lst.house == [["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["NAN", "NAN", "", "NAN", "NAN"],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "NAN", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"],
                          ["", "NAN", "", "NAN", ""],
                          ["NAN", "", "NAN", "", "NAN"]]
    assert p.choosen_dice.current_side in [1, 2, 3, 4, 5, 6]
def test_repr():
    c = Player(name='George', house=House())
    print(c)

def test_choose_dice():
    pass

def test_choose_action():
    pass

def test_save():
    pass

def test_load():
    pass