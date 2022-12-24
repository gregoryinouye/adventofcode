#!/usr/bin/env python3

from pathlib import Path
import sys
from typing import Optional

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 3966
part_two_answer = 933


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_grid(lines: list[str]) -> set[tuple[int, int]]:
    return {(r, c) for r, line in enumerate(lines) for c, cell in enumerate(line) if cell == '#'}


directions = [
    ((-1, 0), (-1, -1), (-1, 1)),
    ((1, 0), (1, -1), (1, 1)),
    ((0, -1), (1, -1), (-1, -1)),
    ((0, 1), (1, 1), (-1, 1)),
]


def has_neighbor(grid: set[tuple[int, int]], position: tuple[int, int]) -> bool:
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
        r, c = position
        if (r + dr, c + dc) in grid:
            return True
    return False


def propose_move(grid: set[tuple[int, int]], position: tuple[int, int], offset: int) -> Optional[tuple[int, int]]:
    r, c = position

    for i in range(4):
        direction_check = directions[(i + offset) % 4]

        if all(map(lambda delta: (r + delta[0], c + delta[1]) not in grid, direction_check)):
            return r + direction_check[0][0], c + direction_check[0][1]

    return None


def update_grid(grid: set[tuple[int, int]], offset: int) -> bool:
    proposed = {}
    conflicts = set()

    for r, c in list(grid):
        if not has_neighbor(grid, (r, c)):
            continue
        destination = propose_move(grid, (r, c), offset % 4)
        if destination is None:
            continue
        if destination in proposed:
            conflicts.add(destination)
        proposed[destination] = (r, c)

    valid_moves = {key: value for key, value in proposed.items() if key not in conflicts}
    grid.difference_update(valid_moves.values())
    grid.update(valid_moves.keys())

    return len(proposed) > 0


def get_min_area(coordinates: list[tuple[int, int]]) -> int:
    min_x, max_x = float('inf'), -float('inf')
    min_y, max_y = float('inf'), -float('inf')

    for x, y in coordinates:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)

    return (max_x - min_x + 1) * (max_y - min_y + 1)


def part_one(lines: list[str]) -> int:
    grid = parse_grid(lines)

    for i in range(10):
        update_grid(grid, i)

    return get_min_area(list(grid)) - len(grid)


def part_two(lines: list[str]) -> int:
    grid = parse_grid(lines)
    delta = True
    i = 0

    while delta:
        delta = update_grid(grid, i)
        i += 1

    return i


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
