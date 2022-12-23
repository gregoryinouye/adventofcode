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
        '.....',
        '..##.',
        '..#..',
        '.....',
        '..##.',
        '.....',
    ]


@pytest.fixture
def test_example_input2():
    return [
        '..............',
        '..............',
        '.......#......',
        '.....###.#....',
        '...#...#.#....',
        '....#...##....',
        '...#.###......',
        '...##.#.##....',
        '....#..#......',
        '..............',
        '..............',
        '..............',
    ]


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 25


def test_part_one_with_example_input_2(test_example_input2):
    assert solution.part_one(test_example_input2) == 110


def test_part_two_with_example_input_2(test_example_input2):
    assert solution.part_two(test_example_input2) == 20


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
