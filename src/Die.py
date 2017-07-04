class Die(object):
    """ This is the Die class"""

    def __init__(self, sides, probs):
        self.sides = sides
        self.probs = probs
        self.pmf = None

    def roll(self):
        """Roll the die and return a side"""
        pass

class BiasedDie(Die):
    """This is the biased die class"""
    pass