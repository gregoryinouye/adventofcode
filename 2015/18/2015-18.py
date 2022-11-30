#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 768
part_two_answer = 0


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def process_grid(lines: list[str], lights: list[list[int]]) -> list[list[int]]:
    for row, line in enumerate(lines):
        for col, value in enumerate(line):
            if value == '#':
                lights[row][col] = 1
    return lights


def count_neighbors(row: int, col: int, grid: list[list[int]]) -> int:
    count = 0

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and abs(grid[row + dr][col + dc]) == 1:
                count += 1

    return count


def step_grid(grid: list[list[int]]) -> list[list[int]]:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count = count_neighbors(row, col, grid)

            if grid[row][col] == 1:
                if count < 2 or count > 3:
                    grid[row][col] = -1
            else:
                if count == 3:
                    grid[row][col] = 2

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == -1:
                grid[row][col] = 0
            elif grid[row][col] == 2:
                grid[row][col] = 1
    return grid


def part_one(lines: list[str], steps: int = 100) -> int:
    grid = process_grid(lines=lines, lights=[[0] * len(lines[0]) for _ in range(len(lines))])

    for i in range(steps):
        step_grid(grid)

    return sum(sum(row) for row in grid)


def part_two(lines: list[str], steps: int = 100) -> int:
    grid = process_grid(lines=lines, lights=[[0] * len(lines[0]) for _ in range(len(lines))])
    m = len(grid) - 1
    n = len(grid[0]) - 1

    for i in range(steps):
        step_grid(grid)
        grid[0][0] = 1
        grid[m][0] = 1
        grid[0][n] = 1
        grid[m][n] = 1

    return sum(sum(row) for row in grid)


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
