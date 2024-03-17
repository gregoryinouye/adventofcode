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
        'seeds: 79 14 55 13',
        'seed-to-soil map:\n50 98 2\n52 50 48',
        'soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15',
        'fertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4',
        'water-to-light map:\n88 18 7\n18 25 70',
        'light-to-temperature map:\n45 77 23\n81 45 19\n68 64 13',
        'temperature-to-humidity map:\n0 69 1\n1 0 69',
        'humidity-to-location map:\n60 56 37\n56 93 4',
    ]


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 35


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 46


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
