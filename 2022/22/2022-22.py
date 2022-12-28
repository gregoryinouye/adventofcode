#!/usr/bin/env python3

from pathlib import Path
import sys
from typing import Callable

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 88226
part_two_answer = 57305


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().rstrip().split('\n\n')


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
convert_char = {'.': 0, '#': 1, ' ': -1}


def parse_path(line: str) -> list[tuple[int, int]]:
    path = []
    rotation = 0
    magnitude = ''

    for char in line:
        if char.isdecimal():
            magnitude += char
        else:
            path.append((rotation, int(magnitude)))
            rotation = 1 if char == 'R' else -1
            magnitude = ''

    path.append((rotation, int(magnitude)))
    return path


def parse_map(lines: list[str]) -> dict[tuple[int, int], int]:
    return {(r, c): convert_char[char] for r, line in enumerate(lines) for c, char in enumerate(line)}


def get_wrap_point(grid: dict[tuple[int, int], int], position: tuple[int, int, int]) -> tuple[int, int, int]:
    r, c, facing = position
    dr, dc = directions[(facing + 2) % 4]

    while grid.get((r + dr, c + dc), -1) > -1:
        r += dr
        c += dc

    return r, c, facing


def get_cube_point(grid: dict[tuple[int, int], int], position: tuple[int, int, int]) -> tuple[int, int, int]:
    r, c, facing = position
    new_r, new_c, new_facing = -1, -1, -1

    if facing == 0:
        if c == 149: # E1
            new_r = 149 - r
            new_c = 99
            new_facing = 2
        elif c == 99 and 50 <= r < 100: # A
            new_r = 49
            new_c = r + 50
            new_facing = 3
        elif c == 99 and 100 <= r < 150: # E2
            new_r = 149 - r
            new_c = 149
            new_facing = 2
        elif c == 49 and 150 <= r < 200: # C
            new_r = 149
            new_c = r - 100
            new_facing = 3
    if facing == 1:
        if r == 49 and 100 <= c < 150: # A
            new_r = c - 50
            new_c = 99
            new_facing = 2
        elif r == 149 and 50 <= c < 100: # C
            new_r = c + 100
            new_c = 49
            new_facing = 2
        elif r == 199: # F
            new_r = 0
            new_c = c + 100
            new_facing = 1
    if facing == 2:
        if c == 50 and 0 <= r < 50: # G1
            new_r = 149 - r
            new_c = 0
            new_facing = 0
        elif c == 50 and 50 <= r < 100: # B
            new_r = 100
            new_c = r - 50
            new_facing = 1
        elif c == 0 and 100 <= r < 150: # G2
            new_r = 149 - r
            new_c = 50
            new_facing = 0
        elif c == 0 and 150 <= r < 200: # D
            new_r = 0
            new_c = r - 100
            new_facing = 1
    if facing == 3:
        if r == 100 and 0 <= c < 50: # B
            new_r = c + 50
            new_c = 50
            new_facing = 0
        elif r == 0 and 50 <= c < 100: # D
            new_r = c + 100
            new_c = 0
            new_facing = 0
        elif r == 0 and 100 <= c < 150: # F
            new_r = 199
            new_c = c - 100
            new_facing = 3

    if grid[new_r, new_c] == 1:
        return r, c, facing

    return new_r, new_c, new_facing


def apply_instruction(
        grid: dict[tuple[int, int], int],
        path: tuple[int, int],
        position: tuple[int, int, int],
        wrap: Callable[[dict, tuple], tuple[int, int, int]],
) -> tuple[int, int, int]:
    rotation, magnitude = path
    r, c, facing = position
    facing = (facing + rotation + 4) % 4
    dr, dc = directions[facing]

    for i in range(magnitude):
        new_r, new_c, new_facing, new_dr, new_dc = r + dr, c + dc, facing, dr, dc

        if grid.get((new_r, new_c), -1) == -1:
            new_r, new_c, new_facing = wrap(grid, (r, c, facing))
            new_dr, new_dc = directions[new_facing]
        if grid[new_r, new_c] == 1 or (new_r, new_c) == (r, c):
            break

        r, c, facing, dr, dc = new_r, new_c, new_facing, new_dr, new_dc

    return r, c, facing


def get_final_password(row: int, col: int, facing: int) -> int:
    return 1000 * row + 4 * col + facing


def part_one(lines: list[str]) -> int:
    grid = parse_map(lines[0].split('\n'))
    paths = parse_path(lines[1])
    r, facing = 0, 0
    _, c = next((r, c) for r, c in grid.keys() if r == 0 and grid[r, c] == 0)

    for path in paths:
        r, c, facing = apply_instruction(grid=grid, path=path, position=(r, c, facing), wrap=get_wrap_point)

    return get_final_password(r + 1, c + 1, facing)


def part_two(lines: list[str]) -> int:
    grid = parse_map(lines[0].split('\n'))
    paths = parse_path(lines[1])
    r, facing = 0, 0
    _, c = next((r, c) for r, c in grid.keys() if r == 0 and grid[r, c] == 0)

    for path in paths:
        r, c, facing = apply_instruction(grid=grid, path=path, position=(r, c, facing), wrap=get_cube_point)

    return get_final_password(r + 1, c + 1, facing)


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
