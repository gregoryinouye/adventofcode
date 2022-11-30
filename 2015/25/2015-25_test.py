import pathlib
import pytest
import importlib

filepath = pathlib.Path(__file__)
day = filepath.stem.split('_')[0]
solution = importlib.import_module(day)


@pytest.fixture
def test_input():
    return solution.parse(solution.test_filepath)


@pytest.mark.parametrize('example,expected', [(20151125, 31916031), (30943339, 77061)])
def test_next_value_with_example_input(example, expected):
    assert solution.next_value(example) == expected


@pytest.mark.parametrize('example,expected', [('row 1, col 2', 18749137), ('row 6, col 1', 33071741)])
def test_next_value_with_example_input(example, expected):
    assert solution.part_one(example) == expected


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


@pytest.mark.skip
def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
