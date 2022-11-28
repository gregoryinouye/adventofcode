import pathlib
import pytest
import importlib

filepath = pathlib.Path(__file__)
day = filepath.stem.split('_')[0]
solution = importlib.import_module(day)


@pytest.fixture
def test_input():
    return solution.parse(solution.test_filepath)


@pytest.mark.parametrize(
    'example,expected',
    [('1', '11'), ('11', '21'), ('21', '1211'), ('111221', '312211')]
)
def test_look_and_say_with_example(example,expected):
    assert solution.look_and_say(example) == expected


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


@pytest.mark.skip
def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
