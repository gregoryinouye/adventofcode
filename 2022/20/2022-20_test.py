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
    return ['1', '2', '-3', '3', '-2', '0', '4']


@pytest.mark.parametrize('number,index,expected', [
    (3, 5, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (6, 6), (7, 7), (8, 8), (5, 3), (9, 9)]),
    (8, 5, [(0, 0), (1, 1), (2, 2), (3, 3), (5, 8), (4, 4), (6, 6), (7, 7), (8, 8), (9, 9)]),
    (-4, 5, [(0, 0), (5, -4), (1, 1), (2, 2), (3, 3), (4, 4), (6, 6), (7, 7), (8, 8), (9, 9)]),
    (-5, 5, [(5, -5), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (6, 6), (7, 7), (8, 8), (9, 9)]),
])
def test_move_value(number, index, expected):
    assert solution.move_value([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, number), (6, 6), (7, 7), (8, 8), (9, 9)], index) == expected


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 3


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 1623178306


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
