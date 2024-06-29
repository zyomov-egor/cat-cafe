from dice import Dice


def test_init():
    c = Dice()
    assert c.sides == [1, 2, 3, 4, 5, 6]
    assert c.side in [1, 2, 3, 4, 5, 6]

def test_repr():
    c = Dice()
    assert type(c) == Dice


def test_roll():
    c = Dice()
    assert