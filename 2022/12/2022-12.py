#!/usr/bin/env python3

from collections import deque
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 468
part_two_answer = 459


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_grid(input_grid: list[str]) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    grid = [[] for _ in range(len(input_grid))]
    starting = -1, -1
    ending = -1, -1

    for r, row in enumerate(input_grid):
        current = grid[r]

        for c, col in enumerate(row):
            if col == 'S':
                col = 'a'
                starting = (r, c)
            if col == 'E':
                col = 'z'
                ending = (r, c)
            current.append(ord(col) - 97)

    return grid, starting, ending


def bfs(grid: list[list[int]], starting: tuple[int, int], ending: tuple[int, int]) -> int:
    steps = {starting: 0}
    next_coordinates = deque([starting])

    while next_coordinates and ending not in steps:
        r, c = next_coordinates.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r = r + dr
            new_c = c + dc
            if (new_r, new_c) in steps or \
                    not 0 <= new_r < len(grid) or \
                    not 0 <= new_c < len(grid[0]) or \
                    grid[new_r][new_c] - grid[r][c] > 1:
                continue
            next_coordinates.append((new_r, new_c))
            steps[(new_r, new_c)] = steps[r, c] + 1

    return steps.get(ending, -1)


def part_one(lines: list[str]) -> int:
    return bfs(*parse_grid(lines))


def part_two(lines: list[str]) -> int:
    grid, starting, ending = parse_grid(lines)
    min_steps = float('inf')

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                result = bfs(grid, (r, c), ending)
                if result != -1:
                    min_steps = min(min_steps, result)

    return min_steps


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
