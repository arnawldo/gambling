import pytest

from src.Die import Die, BiasedDie, NotEnoughSidesError, InvalidProbailitySpaceError


def test__die_is_instance__succeeds():
    die = Die()
    assert type(die) == Die

def test__die_len_sides_equal_len_probs__succeeds():
    die = Die()
    assert len(die.sides) == len(die.probs)
    assert len(die.sides) == len(die.cpmf)

def test__die_probs_not_greater_than_one__succeeds():
    die = Die()
    assert sum(die.probs) < 1

def test__die_sides__less_than_4__raises():
    with pytest.raises(NotEnoughSidesError):
        die = Die(sides=[1, 2], probs=[0.5, 0.5], cpmf=[0.5, 1])

def test__die_probs__less_than_equal_to_1__raises():
    with pytest.raises(InvalidProbailitySpaceError):
        die = Die(sides=[1, 2, 3, 4], probs=[0.5, 0.5, 0.5, 0.5], cpmf=[0.5, 1, 1, 1])



def test__biased_die_len_sides_equal_len_probs__succeeds():
    die = BiasedDie(2)
    assert len(die.sides) == len(die.probs)
    assert len(die.sides) == len(die.cpmf)

def test__biased_die_probs_not_greater_than_one__succeeds():
    die = BiasedDie(2)
    assert sum(die.probs) < 1