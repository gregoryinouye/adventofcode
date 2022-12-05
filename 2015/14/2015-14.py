#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 2655
part_two_answer = 1059


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def process_reindeer_stats(stats: list[str]) -> dict[str, tuple[int, int, int]]:
    processed = {}

    for stat in stats:
        stat_split = stat.split(' ')
        reindeer = stat_split[0]
        fly = int(stat_split[3])
        fly_duration = int(stat_split[6])
        rest_duration = int(stat_split[-2])
        processed[reindeer] = (fly, fly_duration, rest_duration)

    return processed


def calculate_reindeer_distance(reindeer_stats: tuple[int, int, int], race_duration: int) -> int:
    fly, fly_duration, rest_duration = reindeer_stats
    full_cycle_duration = fly_duration + rest_duration

    num_full_cycles = race_duration // full_cycle_duration
    full_cycle_distance = num_full_cycles * fly_duration * fly

    partial_cycle_duration = race_duration % full_cycle_duration
    partial_cycle_distance = min(partial_cycle_duration, fly_duration) * fly

    return full_cycle_distance + partial_cycle_distance


def is_cooldown(fly_duration: int, rest_duration: int, current_time: int) -> bool:
    full_cycle_duration = fly_duration + rest_duration
    partial_time = current_time % full_cycle_duration

    return partial_time >= fly_duration


def part_one(lines: list[str], race_duration: int = 2503) -> int:
    reindeer_stats = process_reindeer_stats(lines)
    return max(calculate_reindeer_distance(stats, race_duration) for stats in reindeer_stats.values())


def part_two(lines: list[str], race_duration: int = 2503) -> int:
    reindeer_stats = process_reindeer_stats(lines)
    reindeer_scores = {reindeer: 0 for reindeer in reindeer_stats.keys()}
    reindeer_distances = {reindeer: 0 for reindeer in reindeer_stats.keys()}

    for sec in range(race_duration):
        for reindeer, stats in reindeer_stats.items():
            fly, fly_duration, rest_duration = stats
            if is_cooldown(fly_duration, rest_duration, sec):
                continue
            reindeer_distances[reindeer] += fly

        leader_distance = max(reindeer_distances.values())

        for reindeer, distance in reindeer_distances.items():
            if distance == leader_distance:
                reindeer_scores[reindeer] += 1

    return max(reindeer_scores.values())


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
