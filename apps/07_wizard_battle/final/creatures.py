import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level
        )
