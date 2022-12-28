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
cube_functions = {
    (0, 0): lambda r, c: (149 - r, 99, 2),
    (1, 0): lambda r, c: (49, r + 50, 3),
    (2, 0): lambda r, c: (149 - r, 149, 2),
    (3, 0): lambda r, c: (149, r - 100, 3),
    (0, 1): lambda r, c: (0, c + 100, 1),
    (1, 1): lambda r, c: (100 + c, 49, 2),
    (2, 1): lambda r, c: (c - 50, 99, 2),
    (0, 2): lambda r, c: (149 - r, 0, 0),
    (1, 2): lambda r, c: (100, r - 50, 1),
    (2, 2): lambda r, c: (149 - r, 50, 0),
    (3, 2): lambda r, c: (0, r - 100, 1),
    (0, 3): lambda r, c: (50 + c, 50, 0),
    (1, 3): lambda r, c: (c + 100, 0, 0),
    (2, 3): lambda r, c: (199, c - 100, 3),
}


def parse_instructions(line: str) -> list[tuple[int, int]]:
    instructions = []
    rotation = 0
    magnitude = ''

    for char in line:
        if char.isdecimal():
            magnitude += char
        else:
            instructions.append((rotation, int(magnitude)))
            rotation = 1 if char == 'R' else -1
            magnitude = ''

    instructions.append((rotation, int(magnitude)))
    return instructions


def parse_map(lines: list[str]) -> dict[tuple[int, int], int]:
    return {(r, c): convert_char[char] for r, line in enumerate(lines) for c, char in enumerate(line)}


def get_edge(position: tuple[int, int, int], edge_length: int) -> int:
    r, c, facing = position
    return r // edge_length if facing % 2 == 0 else c // edge_length


def get_wrap_point(grid: dict[tuple[int, int], int], position: tuple[int, int, int]) -> tuple[int, int, int]:
    r, c, facing = position
    dr, dc = directions[(facing + 2) % 4]

    while grid.get((r + dr, c + dc), -1) > -1:
        r += dr
        c += dc

    return r, c, facing


def get_cube_point(grid: dict[tuple[int, int], int], position: tuple[int, int, int]) -> tuple[int, int, int]:
    r, c, facing = position
    edge = get_edge(position=position, edge_length=50)
    new_r, new_c, new_facing = cube_functions[edge, facing](r, c)

    if grid[new_r, new_c] == 1:
        return position

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
    instructions = parse_instructions(lines[1])
    r, facing = 0, 0
    _, c = next((r, c) for r, c in grid.keys() if r == 0 and grid[r, c] == 0)

    for path in instructions:
        r, c, facing = apply_instruction(grid=grid, path=path, position=(r, c, facing), wrap=get_wrap_point)

    return get_final_password(r + 1, c + 1, facing)


def part_two(lines: list[str]) -> int:
    grid = parse_map(lines[0].split('\n'))
    instructions = parse_instructions(lines[1])
    r, facing = 0, 0
    _, c = next((r, c) for r, c in grid.keys() if r == 0 and grid[r, c] == 0)

    for path in instructions:
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
