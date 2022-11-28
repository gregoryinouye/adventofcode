#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 'vzbxxyzz'
part_two_answer = 'vzcaabcc'


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def increment_password(password: str) -> str:
    result = list(password)
    i = len(result)
    should_increment = True

    while should_increment:
        i -= 1
        should_increment = result[i] == 'z'
        new_char_ord = get_next_allowed_ord(ord(result[i]) + 1)
        result[i] = chr(new_char_ord)

    return ''.join(result)


def get_next_allowed_ord(num: int):
    if num == 105 or num == 108 or num == 111:
        return num + 1
    if num > 122:
        return 97
    return num


def is_valid_password(password: str) -> bool:
    """
    must include one increasing straight of at least three letters (e.g. xyz, bcd, etc)
    must not include i, o, or l
    must contain at least two different, non-overlapping pairs of letters (e.g. aa, bb, zz)
    """
    invalid_letters = {'i', 'o', 'l'}
    num_pairs = 0
    has_consecutive = False
    skip_second_in_pair = False

    for i, letter in enumerate(password):
        if letter in invalid_letters:
            return False
        if i < len(password) - 1:
            if letter == password[i + 1] and not skip_second_in_pair:
                num_pairs += 1
                skip_second_in_pair = True
            else:
                skip_second_in_pair = False
        letter_ord = ord(letter)
        if not 103 <= letter_ord <= 111 and i < len(password) - 2:
            if chr(letter_ord + 1) == password[i + 1] and chr(letter_ord + 2) == password[i + 2]:
                has_consecutive = True

    return num_pairs > 1 and has_consecutive


def part_one(line: str) -> str:
    current = increment_password(line)
    while not is_valid_password(current):
        current = increment_password(current)
    return current


def part_two(line: str) -> str:
    return part_one(part_one(line))


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f"\n{path_str}:")
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input)
        part_two_actual = part_two(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
