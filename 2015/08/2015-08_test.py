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
def test_input_example():
    return ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']


@pytest.mark.parametrize('escaped_string,count',
                         [(['""'], 2), (['"abc"'], 2), (['"aaa\\"aaa"'], 3), (['"\\x27"'], 5)])
def test_part_one_with_example_input_separated(escaped_string, count):
    assert solution.part_one(escaped_string) == count


def test_part_one_with_example_input(test_input_example):
    assert solution.part_one(test_input_example) == 12


def test_part_one_with_complex_example():
    complex_example = ['"byc\\x9dyxuafof\\\\\\xa6uf\\\\axfozomj\\\\olh\\x6a"']
    assert solution.part_one(complex_example) == 14


def test_part_one(test_input):
    assert solution.part_one(test_input) == solution.part_one_answer


@pytest.mark.parametrize('escaped_string,count',
                         [(['""'], 4), (['"abc"'], 4), (['"aaa\\"aaa"'], 6), (['"\\x27"'], 5)])
def test_part_one_with_example_input_separated(escaped_string, count):
    assert solution.part_two(escaped_string) == count


def test_part_two(test_input):
    assert solution.part_two(test_input) == solution.part_two_answer
