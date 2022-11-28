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
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141',
    ]


def test_process_distances_with_example_input(test_example_input):
    expected = {
        'London': [('Dublin', 464), ('Belfast', 518)],
        'Dublin': [('Belfast', 141), ('London', 464)],
        'Belfast': [('Dublin', 141), ('London', 518)]
    }
    assert solution.process_distances(test_example_input) == expected


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 605


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 982


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
