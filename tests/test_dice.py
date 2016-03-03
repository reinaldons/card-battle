
from cb.core import Dice


def test_roll():
    dice = Dice()

    assert dice.side is None

    dice.roll()

    assert dice.side in dice.sides
