import random


class Die(object):
    """ This is the Die class

    A die has a fixed number of sides which are three or more. Rolling a die returns one side based on their
    probability of landing face up
    """

    def __init__(self, sides=[1, 2, 3, 4, 5, 6], probs=[1/6]*6, cpmf=[1/6, 2/6, 3/6, 4/6, 5/6, 6/6]):
        """
        Setup 6 sided unbiased die by default

        :param sides: values of the sides of the die
        :type sides: list
        :param probs: probabilities of each side landing face up,
        :type probs: list
        :param cpmf: cumulative probability mass function
        :type cpmf: list
        """

        if len(sides) > 3:
            self.sides = sides
        else:
            raise NotEnoughSidesError("Die needs at least four sides")

        if sum(probs) > 1:
            raise InvalidProbailitySpaceError("Probabilities must sum to 1 at most")
        else:
            self.probs = probs

        def calc_cpmf(probs):
            """calculates cumulative distribution and returns CDF"""
            init_probs = [probs[0]]
            for i in range(1, len(probs)):
                init_probs.append(init_probs[i - 1] + probs[i])
            return init_probs

        self.cpmf = calc_cpmf(probs=probs)

    def roll(self):
        """Roll the die and return a side according to probability"""

        rolled_prob = random.random() # returns probability -> [0, 1)

        for i, cum_prob in enumerate(self.cpmf):
            if rolled_prob <= cum_prob:
                # if rolled_prob is below cumulative prob, return current side
                return self.sides[i]


class BiasedDie(Die):
    """
    This is the biased die class. Takes in extra parameter to add bias on a given side


    """
    def __init__(self, bias_side_pos, sides=[1, 2, 3, 4, 5, 6], probs=[1/6]*6, cpmf=[1/6, 2/6, 3/6, 4/6, 5/6, 6/6]):
        """
        Setup 6 sided unbiased die by default. Add high bias to a given side

        :param bias_side_pos: index of side to add bias on
        :type bias_side_pos: int
        :param sides: values of the sides of the die
        :type sides: list
        :param probs: probabilities of each side landing face up,
        :type probs: list
        :param cpmf: cumulative probability mass function
        :type cpmf: list

        """
        new_probs= [0.4 / (len(probs) - 1) for _ in probs]
        new_probs[bias_side_pos] = 0.6

        super().__init__(sides, new_probs)





class DieError(Exception):

    def __init__(self, message):
        self.message = message

class NotEnoughSidesError(DieError):
    pass

class InvalidProbailitySpaceError(DieError):
    pass