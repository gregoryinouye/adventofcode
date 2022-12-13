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
    return [
        '[1,1,3,1,1]\n[1,1,5,1,1]',
        '[[1],[2,3,4]]\n[[1],4]',
        '[9]\n[[8,7,6]]',
        '[[4,4],4,4]\n[[4,4],4,4,4]',
        '[7,7,7,7]\n[7,7,7]',
        '[]\n[3]',
        '[[[]]]\n[[]]',
        '[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]'
    ]


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 13


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 140


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
