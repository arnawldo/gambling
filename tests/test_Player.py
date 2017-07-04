import pytest
from src.Player import GeneralPlayer, SmartPlayer, GuessingPlayer


# general player tests
def test__general_player_is_instance__succeeds():
    player = GeneralPlayer()
    assert type(player) == GeneralPlayer


# smart player tests
def test__smart_player_is_instance__succeeds():
    player = GuessingPlayer()
    assert isinstance(player, GeneralPlayer)


def test__smart_player_has_previous_rolls__succeeds():
    player = SmartPlayer()
    assert type(player.previous_rolls) == list


# guessing player tests
def test__guessing_player_is_instance__succeeds():
    player = SmartPlayer()
    assert isinstance(player, GeneralPlayer)
