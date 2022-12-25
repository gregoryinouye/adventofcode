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
        '1=-0-2',
        '12111',
        '2=0=',
        '21',
        '2=01',
        '111',
        '20012',
        '112',
        '1=-1=',
        '1-12',
        '12',
        '1=',
        '122',
    ]


def test_to_base_ten():
    assert solution.to_base_ten('2=-01') == 976


def test_to_base_five():
    assert solution.to_base_five(4890) == '2=-1=0'


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == '2=-1=0'


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer
