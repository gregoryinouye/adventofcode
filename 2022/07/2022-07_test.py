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
        '$ cd /',
        '$ ls',
        'dir a',
        '14848514 b.txt',
        '8504156 c.dat',
        'dir d',
        '$ cd a',
        '$ ls',
        'dir e',
        '29116 f',
        '2557 g',
        '62596 h.lst',
        '$ cd e',
        '$ ls',
        '584 i',
        '$ cd ..',
        '$ cd ..',
        '$ cd d',
        '$ ls',
        '4060174 j',
        '8033020 d.log',
        '5626152 d.ext',
        '7214296 k'
    ]


def test_part_one_with_example_input(test_example_input):
    assert solution.part_one(test_example_input) == 95437


def test_part_two_with_example_input(test_example_input):
    assert solution.part_two(test_example_input) == 24933642


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
