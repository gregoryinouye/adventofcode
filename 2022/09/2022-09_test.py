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
    return ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']


@pytest.fixture
def test_example_input2():
    return ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 13


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 1


def test_part_two_with_example_input2(test_example_input2):
    assert solution.part_two(test_example_input2) == 36


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
