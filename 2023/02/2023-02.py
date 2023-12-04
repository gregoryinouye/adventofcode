#!/usr/bin/env python3

import math
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 2679
part_two_answer = 77607


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_games(input: list[str]) -> list[list[dict[str, int]]]:
    games = [game.split(':')[1].split(';') for game in input]

    parsed = []
    for game in games:
        current = []
        for time in game:
            count = [count_color.split(' ') for count_color in time.strip().split(', ')]
            current.append({color: num for num, color in count})
        parsed.append(current)
    return parsed


def get_max(game: list[dict[str, int]]) -> dict[str, int]:
    result = dict()
    for time in game:
        for key, value in time.items():
            result[key] = max(result.get(key, 0), int(value))
    return result


def is_possible(game_max: dict[str, int], max_cubes: dict[str, int]) -> bool:
    return all([game_max[key] <= max_cubes[key] for key in game_max.keys()])


def part_one(lines: list[str]) -> int:
    parsed = parse_games(lines)
    game_maxes = [get_max(game) for game in parsed]
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    indices = [index + 1 for index, game in enumerate(game_maxes) if is_possible(game, max_cubes)]
    return sum(indices)


def part_two(lines: list[str]) -> int:
    parsed = parse_games(lines)
    game_maxes = [get_max(game) for game in parsed]
    multiples = [math.prod(game_max.values()) for game_max in game_maxes]
    return sum(multiples)


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
