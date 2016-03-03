
import random


ATTRIBUTES = {
    'attack': 'Simple attack',
    'defense': 'Simple defense',
    'fire': 'Mana for fire skill',
    'water': 'Mana for water skill',
    'earth': 'Mana for earth skill',
    'wind': 'Mana for wind skill',
}


class Dice:

    def __init__(self):
        self.sides = list(ATTRIBUTES.keys())
        self.side = None

    def roll(self):
        self.side = random.choice(self.sides)
