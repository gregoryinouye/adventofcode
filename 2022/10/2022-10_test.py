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
def test_example_input2():
    return ['addx 15', 'addx -11', 'addx 6', 'addx -3', 'addx 5', 'addx -1', 'addx -8', 'addx 13', 'addx 4', 'noop',
            'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx -35',
            'addx 1', 'addx 24', 'addx -19', 'addx 1', 'addx 16', 'addx -11', 'noop', 'noop', 'addx 21', 'addx -15',
            'noop', 'noop', 'addx -3', 'addx 9', 'addx 1', 'addx -3', 'addx 8', 'addx 1', 'addx 5', 'noop', 'noop',
            'noop', 'noop', 'noop', 'addx -36', 'noop', 'addx 1', 'addx 7', 'noop', 'noop', 'noop', 'addx 2', 'addx 6',
            'noop', 'noop', 'noop', 'noop', 'noop', 'addx 1', 'noop', 'noop', 'addx 7', 'addx 1', 'noop', 'addx -13',
            'addx 13', 'addx 7', 'noop', 'addx 1', 'addx -33', 'noop', 'noop', 'noop', 'addx 2', 'noop', 'noop', 'noop',
            'addx 8', 'noop', 'addx -1', 'addx 2', 'addx 1', 'noop', 'addx 17', 'addx -9', 'addx 1', 'addx 1',
            'addx -3', 'addx 11', 'noop', 'noop', 'addx 1', 'noop', 'addx 1', 'noop', 'noop', 'addx -13', 'addx -19',
            'addx 1', 'addx 3', 'addx 26', 'addx -30', 'addx 12', 'addx -1', 'addx 3', 'addx 1', 'noop', 'noop', 'noop',
            'addx -9', 'addx 18', 'addx 1', 'addx 2', 'noop', 'noop', 'addx 9', 'noop', 'noop', 'noop', 'addx -1',
            'addx 2', 'addx -37', 'addx 1', 'addx 3', 'noop', 'addx 15', 'addx -21', 'addx 22', 'addx -6', 'addx 1',
            'noop', 'addx 2', 'addx 1', 'noop', 'addx -10', 'noop', 'noop', 'addx 20', 'addx 1', 'addx 2', 'addx 2',
            'addx -6', 'addx -11', 'noop', 'noop', 'noop']


def test_part_one_with_example_input2(test_example_input2):
    assert solution.part_one(test_example_input2) == 13140


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
