#!/usr/bin/env python3

from typing import Callable
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 2547
part_two_answer = 1939


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def get_grid_rc(grid: list[str]) -> tuple[int, int]:
    return len(grid), len(grid[0])


def is_valid(row: int, column: int, grid_rc: tuple[int, int]) -> bool:
    return 0 <= row < grid_rc[0] and 0 <= column < grid_rc[1]


def is_word(start_rc: tuple[int, int], direction: tuple[int, int], grid: list[str]) -> bool:
    row, col = start_rc
    grid_rc = get_grid_rc(grid)
    dr, dc = direction

    for letter in 'XMAS':
        if not is_valid(row, col, grid_rc) or grid[row][col] != letter:
            return False
        row, col = row + dr, col + dc
    return True


def check_point(row: int, column: int, grid: list[str]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    return sum([1 for direction in directions if is_word((row, column), direction, grid)])


def is_cross(row: int, col: int, grid: list[str]) -> bool:
    grid_rc = get_grid_rc(grid)
    ms_set = {'M', 'S'}

    if grid[row][col] != 'A':
        return False

    for (dr1, dc1, dr2, dc2) in [(1, 1, -1, -1), (-1, 1, 1, -1)]:
        point1, point2 = (dr1 + row, dc1 + col), (dr2 + row, dc2 + col)
        if not is_valid(*point1, grid_rc=grid_rc) or not is_valid(*point2, grid_rc=grid_rc):
            return False
        letter1, letter2 = grid[point1[0]][point1[1]], grid[point2[0]][point2[1]]
        if letter1 == letter2 or letter1 not in ms_set or letter2 not in ms_set:
            return False
    return True


def count_xmas(lines: list[str], func: Callable[[int, int, list[str]], int]) -> int:
    grid_rc = get_grid_rc(lines)

    total = 0
    for row in range(grid_rc[0]):
        for col in range(grid_rc[1]):
            total += func(row, col, lines)
    return total


def part_one(lines: list[str]) -> int:
    return count_xmas(lines, check_point)


def part_two(lines: list[str]) -> int:
    return count_xmas(lines, is_cross)


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
