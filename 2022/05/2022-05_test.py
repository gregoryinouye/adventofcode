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
    return '    [D]    \n' \
           '[N] [C]    \n' \
           '[Z] [M] [P]\n' \
           ' 1   2   3 \n' \
           '\n' \
           'move 1 from 2 to 1\n' \
           'move 3 from 1 to 3\n' \
           'move 2 from 2 to 1\n' \
           'move 1 from 1 to 2'


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 'CMZ'


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 'MCD'


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
