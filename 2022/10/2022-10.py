#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 14720
part_two_answer = '####.####.###..###..###..####.####.####.#.......#.#..#.#..#.#..#.#.......#.#....###....#..###..#..#.###..###....#..###..#.....#...#..#.###..#..#.#.....#...#....#....#....#..#.#....#..#.#....#....#....#....####.###..#....###..#....####.#....'
# FZBPBFZF


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(lines: list[str]) -> int:
    check = {20, 60, 100, 140, 180, 220}
    cycle = 0
    register = 1
    result = 0

    for line in lines:
        cycle += 1
        if cycle in check:
            result += cycle * register

        command = line.split(' ')
        if command[0].startswith('addx'):
            cycle += 1
            if cycle in check:
                result += cycle * register
            register += int(command[1])

    return result


def part_two(lines: list[str]) -> str:
    cycle = 0
    register = 1
    result = []

    for line in lines:
        result.append('#' if abs(cycle % 40 - register) <= 1 else '.')
        cycle += 1

        command = line.split(' ')
        if command[0].startswith('addx'):
            result.append('#' if abs(cycle % 40 - register) <= 1 else '.')
            cycle += 1
            register += int(command[1])

    for i in range(0, 240, 40):
        print(result[i: i + 40])

    return ''.join(result)


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
