#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 763
part_two_answer = 23921


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def build_scan(lines: list[str]) -> dict[tuple[int, int], int]:
    cave = {}

    for line in lines:
        xy_pairs = [tuple(map(int, point.split(','))) for point in line.split(' -> ')]
        for i in range(1, len(xy_pairs)):
            start, end = xy_pairs[i - 1], xy_pairs[i]
            draw_line(cave=cave, start=start, end=end)

    return cave


def draw_line(cave: dict[tuple[int, int], int], start: tuple[int, int], end: tuple[int, int]) -> None:
    (x1, y1), (x2, y2) = start, end

    if x1 == x2:
        min_y, max_y = min(y1, y2), max(y1, y2)
        for j in range(min_y, max_y + 1):
            cave[(x1, j)] = 2

    if y1 == y2:
        min_x, max_x = min(x1, x2), max(x1, x2)
        for j in range(min_x, max_x + 1):
            cave[(j, y1)] = 2


def drop_sand(cave: dict[tuple[int, int], int], origin: tuple[int, int], max_height: int, has_floor: bool) -> tuple[int, int]:
    landing = get_landing(cave=cave, origin=origin, max_height=max_height, has_floor=has_floor)

    if landing[1] >= 0:
        cave[landing] = 1

    return landing


def get_landing(cave: dict[tuple[int, int], int], origin: tuple[int, int], max_height: int, has_floor: bool) -> tuple[int, int]:
    current = origin

    while current[1] < max_height:
        x, y  = current
        new_y = y + 1

        if cave.get((x, new_y), 0) == 0:
            current = x, new_y
        elif cave.get((x - 1, new_y), 0) == 0:
            current = x - 1, new_y
        elif cave.get((x + 1, new_y), 0) == 0:
            current = x + 1, new_y
        else:
            break

    return current if current[1] < max_height or has_floor else (-1, -1)


def get_max_height(lines: list[str]) -> int:
    y = [point.split(',')[1] for line in lines for point in line.split(' -> ')]
    return max(map(int, y))


def part_one(lines: list[str]) -> int:
    cave = build_scan(lines)
    origin = (500, 0)
    cave_height = get_max_height(lines) + 2
    last = (1, 1)

    while last[1] > 0:
        last = drop_sand(cave=cave, origin=origin, max_height=cave_height, has_floor=False)

    return sum(filter(lambda value: value == 1, cave.values()))


def part_two(lines: list[str]) -> int:
    cave_height = get_max_height(lines) + 1
    cave = build_scan(lines)
    origin = (500, 0)
    last = (1, 1)

    while last[1] > 0:
        last = drop_sand(cave=cave, origin=origin, max_height=cave_height, has_floor=True)

    return sum(filter(lambda value: value == 1, cave.values()))


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
