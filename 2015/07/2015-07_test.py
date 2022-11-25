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
def test_part_two_input(test_input):
    return solution.modify_data_for_part_two(test_input)


@pytest.fixture
def test_example_input():
    return [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]


@pytest.mark.parametrize('wire,expected',
                         [('d', 72), ('e', 507), ('f', 492), ('g', 114), ('h', 65412), ('i', 65079), ('x', 123),
                          ('y', 456)])
def test_part_one_with_example(test_example_input, wire, expected):
    assert solution.part_one(test_example_input, wire) == expected


def test_part_one(test_input):
    assert solution.part_one(test_input, 'a') == solution.part_one_answer


def test_part_two(test_part_two_input):
    assert solution.part_two(test_part_two_input, 'a') == solution.part_two_answer
