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
    return 'R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2'


@pytest.fixture
def test_example_input2():
    return 'R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20'


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
