import pathlib
import pytest
import importlib


filepath = pathlib.Path(__file__)
day = filepath.stem.split('_')[0]
solution = importlib.import_module(day)


@pytest.fixture
def test_input():
    return solution.parse(solution.test_filepath)


def test_part1_example1(test_input):
    assert solution.part_one(test_input) == 232


def test_part2_example2(test_input):
    assert solution.part_two(test_input) == 1783
