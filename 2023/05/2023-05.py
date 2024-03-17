#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 579439039
part_two_answer = -1


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n\n')


def parse_seeds_part_one(seeds: str) -> list[int]:
    return [int(seed) for seed in seeds.split(':')[1].split()]


def parse_seeds_part_two(seeds: str) -> list[int]:
    seed_ranges = [int(seed) for seed in seeds.split(':')[1].split()]
    result = []
    for index in range(0, len(seed_ranges), 2):
        start, length = seed_ranges[index:index + 2]
        result.extend(range(start, start + length))
    return result


def parse_map(value_map: str) -> list[(int, int, int, dict[int, int])]:
    raw_maps = value_map.split('\n')[1:]
    maps = [tuple(map(int, raw_map.split())) + tuple(dict()) for raw_map in raw_maps]
    return sorted(maps, key=lambda value_map: value_map[1])


def convert(identifier: int, value_map: list[(int, int, int)]) -> int:
    for (destination, source, length) in value_map:
        if identifier < source:
            break
        if source <= identifier < source + length:
            return destination + identifier - source
    return identifier


def part_one(lines: list[str]) -> int:
    seeds = parse_seeds_part_one(lines[0])
    maps = list(map(parse_map, lines[1:]))

    result = []
    for seed in seeds:
        identifier = seed
        for value_map in maps:
            identifier = convert(identifier, value_map)
        result.append(identifier)
    return min(result)


# currently broken, tried memoizing and quitting on history,
# but this still times out.
# need to evaluate ranges of numbers instead of 1 by 1
def part_two(lines: list[str]) -> int:
    seeds = parse_seeds_part_two(lines[0])
    maps = list(map(parse_map, lines[1:]))

    result = []
    for seed in seeds:
        identifier = seed
        for value_map in maps:
            identifier = convert(identifier, value_map)
        result.append(identifier)
    return min(result)


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
