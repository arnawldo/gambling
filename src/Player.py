import random
from collections import Counter


class GeneralPlayer(object):

    def __init__(self):
        self.previous_guesses = []
        self.current_winnings = 0

    def take_a_guess(self, die):
        pass

class GuessingPlayer(GeneralPlayer):

    def take_a_guess(self, die):

        player_guess = random.choice(die.sides)
        die_roll = die.roll()
        if player_guess == die_roll:
            self.current_winnings += 1

class SmartPlayer(GeneralPlayer):

    def take_a_guess(self, die):

        if len(self.previous_guesses) == 0:
            player_guess = random.choice(die.sides)
        else:
            most_common_side = Counter(self.previous_guesses).most_common(1)
            player_guess = most_common_side[0][0]
        die_roll = die.roll()
        if player_guess == die_roll:
            self.current_winnings += 1

