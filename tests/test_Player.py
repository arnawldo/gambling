import pytest
from src.Player import GeneralPlayer, SmartPlayer, GuessingPlayer

def test__general_player_is_instance__succeeds():
    player = GeneralPlayer()
    assert type(player) == GeneralPlayer

def test__smart_player_is_instance__succeeds():
    player = GuessingPlayer()
    assert isinstance(player, GeneralPlayer)

def test__guessing_player_is_instance__succeeds():
    player = SmartPlayer()
    assert isinstance(player, GeneralPlayer)
