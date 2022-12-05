#!/usr/bin/env python3

import sys
from math import inf
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 117
part_two_answer = 909


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def process_distances(distances: list[str]) -> dict[str, list[tuple[str, int]]]:
    processed = {}
    for distance in distances:
        start, _, end, _, miles = distance.split(' ')
        miles = int(miles)
        dist_array = processed.get(start, [])
        dist_array.append((end, miles))
        processed[start] = dist_array

        reverse_array = processed.get(end, [])
        reverse_array.append((start, miles))
        processed[end] = reverse_array

    for distances in processed.values():
        distances.sort(key=lambda pair: pair[1])

    return processed


def part_one(distance_data: list[str]) -> int:
    distances: dict[str, list[tuple[str, int]]] = process_distances(distance_data)
    min_so_far = inf

    for start in distances.keys():
        current = start
        visited: set[str] = {start}
        path_distances = []

        while len(visited) < len(distances.keys()):
            next_destination = next(filter(lambda distance: distance[0] not in visited, distances.get(current)))
            path_distances.append(next_destination[1])
            current = next_destination[0]
            visited.add(current)

        next_destination = next(filter(lambda distance: distance[0] == start, distances.get(current)))
        path_distances.append(next_destination[1])
        min_so_far = min(min_so_far, sum(path_distances) - max(path_distances))

    return min_so_far


def part_two(distance_data: list[str]) -> int:
    distances: dict[str, list[tuple[str, int]]] = process_distances(distance_data)
    for value in distances.values():
        value.reverse()
    max_so_far = 0

    for start in distances.keys():
        current = start
        path_distances = []
        visited: set[str] = {start}

        while len(visited) < len(distances.keys()):
            next_destination = next(filter(lambda distance: distance[0] not in visited, distances.get(current)))
            path_distances.append(next_destination[1])
            current = next_destination[0]
            visited.add(current)

        next_destination = next(filter(lambda distance: distance[0] == start, distances.get(current)))
        path_distances.append(next_destination[1])
        max_so_far = max(max_so_far, sum(path_distances) - min(path_distances))

    return max_so_far


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
