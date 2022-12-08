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
    return '30373\n25512\n65332\n33549\n35390'


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 21


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 8


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
