import random
from collections import Counter


class GeneralPlayer(object):

    """
    Class for general player
    Attributes:
        current_winnings: total of correct guesses made
    """
    def __init__(self):
        self.current_winnings = 0

    def take_a_guess(self, die):
        """Method to override by subclasses with different techniques"""
        pass

class GuessingPlayer(GeneralPlayer):

    def take_a_guess(self, die):
        """
        Makes random guess of which side of die rolls up.
        """
        player_guess = random.choice(die.sides) # pick random side of die
        die_roll = die.roll()
        if player_guess == die_roll:
            self.current_winnings += 1

class SmartPlayer(GeneralPlayer):
    """
        Class for smart player. Uses past experience to make better guesses

        Attributes:
            current_winnings: total of correct guesses made
            previous_rolls: record of sides rolled by die
        """
    def __init__(self):
        super().__init__()
        self.previous_rolls = []


    def take_a_guess(self, die):

        if len(self.previous_rolls) == 0:
            player_guess = random.choice(die.sides) # if no guess has been made yet, pick randomly
        else:
            # most occuring element
            most_common_side = Counter(self.previous_rolls).most_common(1) # eg [(6, 200)] -> 6 appears 200 times
            player_guess = most_common_side[0][0]

        die_roll = die.roll()
        # record current roll
        self.previous_rolls.append(die_roll)

        if player_guess == die_roll:
            self.current_winnings += 1

