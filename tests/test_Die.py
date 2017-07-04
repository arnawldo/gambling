import pytest

from src.Die import Die


def test__die_is_instance__succeeds():
    die = Die()
    assert type(die) == Die

def test__len_sides_equal_len_probs__succeeds():
    die = Die()
    assert len(die.sides) == len(die.probs)
    assert len(die.sides) == len(die.cpmf)