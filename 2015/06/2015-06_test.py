import pathlib
import pytest
import importlib


filepath = pathlib.Path(__file__)
day = filepath.stem.split('_')[0]
solution = importlib.import_module(day)


@pytest.fixture
def test_input():
    return solution.parse(solution.test_filepath)


def test_part_one_with_example_input1():
    assert solution.part_one(['turn on 0,0 through 999,999']) == 1_000_000


def test_part_one_with_example_input2():
    assert solution.part_one(['toggle 0,0 through 999,0']) == 1_000


def test_part_one_with_example_input3():
    assert solution.part_one(['turn on 0,0 through 999,999', 'turn off 499,499 through 500,500']) == 999_996


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
