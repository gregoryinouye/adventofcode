import pathlib
import pytest
import importlib

filepath = pathlib.Path(__file__)
day = filepath.stem.split('_')[0]
solution = importlib.import_module(day)


@pytest.fixture
def test_input():
    return solution.parse(solution.test_filepath)


@pytest.fixture
def test_example_input():
    return 'Sue 1: goldfish: 9, cars: 0, samoyeds: 9'


def test_process_stats_with_example_input(test_example_input):
    assert solution.process_stats(test_example_input) == solution.SueStats(id=1, goldfish=9, cars=0, samoyeds=9)


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
