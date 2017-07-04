from src.Die import Die, BiasedDie
from src.Player import GuessingPlayer, SmartPlayer

def winnings_with_biased_die(n_iterations):

    # setup die
    die = BiasedDie(3)
    smart_player = SmartPlayer()
    guessing_player = GuessingPlayer()

