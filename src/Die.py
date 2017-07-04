class Die(object):
    """ This is the Die class

    A die has a fixed number of sides which are three or more. Rolling a die returns one side based on their
    probability of landing face up

    :param sides: values of the sides of the die
    :rtype sides: list
    :param probs: probabilities of each side landing face up,
    :rtype probs: list
    :param cpmf: cumulative probability mass function
    :rtype cpmf: list
    """

    def __init__(self, sides=[1, 2, 3, 4, 5, 6], probs=[1/6]*6, cpmf=[1/6, 2/6, 3/6, 4/6, 5/6, 6/6]):

        self.sides = sides
        self.probs = probs
        def calc_cpmf(probs):
            init_probs = [probs[0]]
            for i in range(1, len(probs)):
                init_probs.append(init_probs[i - 1] + probs[i])
            return init_probs

        self.cpmf = calc_cpmf(probs=probs)

    def roll(self):
        """Roll the die and return a side according to probability"""
        pass

class BiasedDie(Die):
    """This is the biased die class

    """


class DieError(Exception):

    def __init__(self, message):
        self.message = message

class NotEnoughSidesError(DieError):
    pass


if __name__ == "__main__":
    die = Die()
    print(die.sides)
    print(die.probs)
    print(die.cpmf)