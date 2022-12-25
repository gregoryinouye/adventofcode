#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = '2=-0=01----22-0-1-10'


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def to_base_ten(base_five: str) -> int:
    numbers = []
    for i in range(len(base_five)):
        current = base_five[i]
        base = pow(5, len(base_five) - i - 1)
        if current.isdecimal():
            numbers.append(int(current) * base)
        elif current == '-':
            numbers.append(-1 * base)
        elif current == '=':
            numbers.append(-2 * base)
    return sum(numbers)

def to_base_five(base_ten: int) -> str:
    number = []
    build = []
    current = base_ten

    while current != 0:
        number.append(current % 5)
        current //= 5

    carry = 0
    for n in number:
        current = n + carry
        if current > 2:
            carry = 1
            build.append(current - 5)
        else:
            build.append(current)
            carry = 0

    return ''.join(str(n) if n >= 0 else '-' if n == -1 else '=' for n in reversed(build))


def part_one(lines: list[str]) -> str:
    numbers = [to_base_ten(line) for line in lines]
    return to_base_five(sum(numbers))


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f'\n{path_str}:')
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
