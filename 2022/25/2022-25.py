#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = '2=-0=01----22-0-1-10'


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


decode_base_five = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
encode_base_five_remainder = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}


def to_base_ten(base_five: str) -> int:
    return sum(decode_base_five[char] * 5 ** (len(base_five) - i - 1) for i, char in enumerate(base_five))


def to_base_five(base_ten: int) -> str:
    base_five_number = []

    while base_ten:
        base_five_number += encode_base_five_remainder[base_ten % 5]
        base_ten = (base_ten + 2) // 5

    return ''.join(base_five_number[::-1])


def part_one(lines: list[str]) -> str:
    total_sum = sum(to_base_ten(line) for line in lines)
    return to_base_five(total_sum)


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f'\n{path_str}:')
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
