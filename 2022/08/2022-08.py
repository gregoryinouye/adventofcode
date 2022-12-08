#!/usr/bin/env python3

import math
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 1870
part_two_answer = 517440


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def left_to_right(grid, output):
    for r in range(len(grid)):
        tallest = -1
        for c in range(len(grid[0])):
            current = int(grid[r][c])

            if current > tallest:
                output[r][c] = 1
                tallest = current


def right_to_left(grid, output):
    for r in range(len(grid)):
        tallest = -1
        for c in range(len(grid[0]) - 1, -1, -1):
            current = int(grid[r][c])

            if current > tallest:
                output[r][c] = 1
                tallest = current


def top_to_bottom(grid, output):
    for c in range(len(grid[0])):
        tallest = -1
        for r in range(len(grid)):
            current = int(grid[r][c])

            if current > tallest:
                output[r][c] = 1
                tallest = current


def bottom_to_top(grid, output):
    for c in range(len(grid[0])):
        tallest = -1
        for r in range(len(grid) - 1, 0, -1):
            current = int(grid[r][c])

            if current > tallest:
                output[r][c] = 1
                tallest = current


def part_one(lines: str) -> int:
    lines_split = lines.split('\n')

    output_grid = [[0] * len(lines_split[0]) for _ in lines_split]

    left_to_right(lines_split, output_grid)
    right_to_left(lines_split, output_grid)
    top_to_bottom(lines_split, output_grid)
    bottom_to_top(lines_split, output_grid)

    return sum(sum(row) for row in output_grid)


def to_right(grid, r, c) -> int:
    current = int(grid[r][c])
    count = 0

    for new_c in range(c + 1, len(grid[0])):
        if int(grid[r][new_c]) < current:
            count += 1
        else:
            count += 1
            break

    return count


def to_left(grid, r, c) -> int:
    current = int(grid[r][c])
    count = 0

    for new_c in range(c - 1, -1, -1):
        if int(grid[r][new_c]) < current:
            count += 1
        else:
            count += 1
            break

    return count


def to_bottom(grid, r, c) -> int:
    current = int(grid[r][c])
    count = 0

    for new_r in range(r + 1, len(grid)):
        if int(grid[new_r][c]) < current:
            count += 1
        else:
            count += 1
            break

    return count


def to_top(grid, r, c) -> int:
    current = int(grid[r][c])
    count = 0

    for new_r in range(r - 1, -1, -1):
        if int(grid[new_r][c]) < current:
            count += 1
        else:
            count += 1
            break

    return count


def get_scenic_score(grid, r, c) -> int:
    right = to_right(grid, r, c)
    left = to_left(grid, r, c)
    bottom = to_bottom(grid, r, c)
    top = to_top(grid, r, c)

    return math.prod((right, left, bottom, top))


def part_two(lines: str) -> int:
    lines_split = lines.split('\n')
    grid = [list(line) for line in lines_split]
    maximum = -1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            score = get_scenic_score(grid, r, c)
            maximum = max(score, maximum)

    return maximum


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
