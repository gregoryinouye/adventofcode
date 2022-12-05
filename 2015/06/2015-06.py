#!/usr/bin/env python3

from pathlib import Path
import re
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 569999
part_two_answer = 17836115


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(instructions: list[str]) -> int:
    lights = [[0] * 1000 for _ in range(1000)]

    for instruction in instructions:
        command, x1_str, y1_str, x2_str, y2_str = re.sub('turn | through', '', instruction).replace(',', ' ').split(' ')

        for x in range(int(x1_str), int(x2_str) + 1):
            for y in range(int(y1_str), int(y2_str) + 1):
                if command == 'off':
                    lights[x][y] = 0
                elif command == 'on':
                    lights[x][y] = 1
                elif command == 'toggle':
                    lights[x][y] = int(not lights[x][y])
                else:
                    raise Exception('unknown command')

    return sum(sum(row) for row in lights)


def part_two(instructions: list[str]) -> int:
    lights = [[0] * 1000 for _ in range(1000)]

    for instruction in instructions:
        command, x1_str, y1_str, x2_str, y2_str = re.sub('turn | through', '', instruction).replace(',', ' ').split(' ')

        for x in range(int(x1_str), int(x2_str) + 1):
            for y in range(int(y1_str), int(y2_str) + 1):
                if command == 'off':
                    lights[x][y] = lights[x][y] - 1 if lights[x][y] > 0 else 0
                elif command == 'on':
                    lights[x][y] += 1
                elif command == 'toggle':
                    lights[x][y] += 2
                else:
                    raise Exception('unknown command')

    return sum(sum(row) for row in lights)


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f'\n{path_str}:')
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input)
        part_two_actual = part_two(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
