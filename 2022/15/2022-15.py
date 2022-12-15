#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 5461729
part_two_answer = 10621647166538


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_locations(lines: list[str]) -> dict[tuple[int, int], tuple[int, int]]:
    locations = {}
    format_location = lambda n: int(n.strip('xy=:,'))

    for line in lines:
        line_split = line.split(' ')
        sensor = format_location(line_split[2]), format_location(line_split[3])
        beacon = format_location(line_split[8]), format_location(line_split[9])
        locations[sensor] = beacon

    return locations


def get_manhattan_distance(point_one: tuple[int, int], point_two: tuple[int, int]) -> int:
    (x1, y1), (x2, y2) = point_one, point_two
    return abs(y2 - y1) + abs(x2 - x1)


def get_outside_range(point: tuple[int, int], distance: int, min_xy: int, max_xy: int) -> iter:
    for dx in range(-distance - 1, distance + 2):
        for dy in [distance + 1 - abs(dx), abs(dx) - distance - 1]:
            if not min_xy <= point[0] + dx <= max_xy or not min_xy <= point[1] + dy <= max_xy:
                continue
            yield point[0] + dx, point[1] + dy


def get_manhattan_range_for_target_y(point: tuple[int, int], distance: int, y: int) -> set[tuple[int, int]]:
    dy = point[1] - y
    return {(point[0] + dx, y) for dx in range(abs(dy) - distance, distance - abs(dy) + 1)}


def part_one(lines: list[str], y: int = 2000000) -> int:
    locations = parse_locations(lines)
    sensor_distances = {sensor: get_manhattan_distance(sensor, beacon) for sensor, beacon in locations.items()}
    within_min_distance = set()

    for sensor, distance in sensor_distances.items():
        within_min_distance.update(get_manhattan_range_for_target_y(sensor, distance, y))

    return len(within_min_distance) - len(within_min_distance.intersection(locations.values()))


def part_two(lines: list[str], max_range: int = 4000000) -> int:
    locations = parse_locations(lines)
    sensor_distances = {sensor: get_manhattan_distance(sensor, beacon) for sensor, beacon in locations.items()}

    for sensor, distance in sensor_distances.items():
        for possible in get_outside_range(sensor, distance, 0, max_range):
            passed = True
            for check_sensor, with_distance in sensor_distances.items():
                if get_manhattan_distance(possible, check_sensor) <= with_distance:
                    passed = False
                    break
            if passed:
                return possible[0] * 4_000_000 + possible[1]
    return -1


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
