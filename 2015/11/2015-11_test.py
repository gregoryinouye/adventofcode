import pathlib
import pytest
import importlib

filepath = pathlib.Path(__file__)
day = filepath.stem.split('_')[0]
solution = importlib.import_module(day)


@pytest.fixture
def test_input():
    return solution.parse(solution.test_filepath)


@pytest.mark.parametrize('example,expected', [('aaa', 'aab'), ('aaz', 'aba'), ('bzz', 'caa')])
def test_increment_password(example, expected):
    assert solution.increment_password(example) == expected


def test_is_valid_password_with_invalid_letters():
    assert solution.is_valid_password('hijklmmn') is False


def test_is_valid_password_with_no_consecutive_straight():
    assert solution.is_valid_password('abbceffg') is False


def test_is_valid_password_with_only_one_pair():
    assert solution.is_valid_password('abbcegjk') is False


@pytest.mark.parametrize('example', ['abcdffaa', 'ghjaabcc'])
def test_is_valid_password_with_valid_input(example):
    assert solution.is_valid_password(example) is True


def test_part_one_with_example_input():
    assert solution.part_one('abcdefgh') == 'abcdffaa'


def test_part_one_with_example_input_two():
    assert solution.part_one('ghijklmn') == 'ghjaabcc'


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
