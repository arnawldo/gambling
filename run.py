import sys
import matplotlib.pyplot as plt

from src.Die import Die, BiasedDie
from src.Player import GuessingPlayer, SmartPlayer

def plot_winnings(n_iterations):

    # setup parameters
    biased_die = BiasedDie(2)
    unbiased_die = Die()
    smart_player = SmartPlayer()
    smart_player_cumulative_win = []
    guessing_player = GuessingPlayer()
    guessing_player_cumulative_win = []

    # run simulation biased die
    for _ in range(n_iterations):
        smart_player.take_a_guess(biased_die)
        smart_player_cumulative_win.append(smart_player.current_winnings)
        guessing_player.take_a_guess(biased_die)
        guessing_player_cumulative_win.append(guessing_player.current_winnings)
        
    fig, axes = plt.subplots(nrows=2)
    

    axes[0].plot(range(n_iterations), smart_player_cumulative_win, label="Smart player")
    axes[0].plot(range(n_iterations), guessing_player_cumulative_win, label="Guessing player")
    axes[0].set_title("Using a biased die")
    axes[0].set_xlabel("number of iterations")
    axes[0].set_ylabel("number of correct guesses")
    axes[0].legend(loc="best")

    # run simulation unbiased die
    smart_player_cumulative_win = []
    guessing_player_cumulative_win = []
    
    for _ in range(n_iterations):
        smart_player.take_a_guess(unbiased_die)
        smart_player_cumulative_win.append(smart_player.current_winnings)
        guessing_player.take_a_guess(unbiased_die)
        guessing_player_cumulative_win.append(guessing_player.current_winnings)
        
    axes[1].plot(range(n_iterations), smart_player_cumulative_win, label="Smart player")
    axes[1].plot(range(n_iterations), guessing_player_cumulative_win, label="Guessing player")
    axes[1].set_title("Using an unbiased die")
    axes[1].set_xlabel("number of iterations")
    axes[1].set_ylabel("number of correct guesses")
    axes[1].legend(loc="best")


    plt.show()



if __name__ == "__main__":
    try:
        n_iterations = int(sys.argv[1])
    except IndexError:
        n_iterations = 1000
    plot_winnings(n_iterations)