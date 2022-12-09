#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 5878
part_two_answer = 2405


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def get_tail_move(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    head_r, head_c = head
    tail_r, tail_c = tail

    if max(abs(head_c - tail_c), abs(head_r - tail_r)) < 2:
        return 0, 0

    delta_r = max(min(1, head_r - tail_r), -1)
    delta_c = max(min(1, head_c - tail_c), -1)

    return delta_r, delta_c


def find_tail_positions(lines: list[str], num_knots: int = 2) -> set[tuple[int, int]]:
    positions = set()
    knots = [{'r': 0, 'c': 0} for _ in range(num_knots)]

    for command in lines:
        direction, magnitude = command.split(' ')
        distance = int(magnitude)

        vector = directions[direction]

        for i in range(distance):
            knots[0]['r'] += vector[0]
            knots[0]['c'] += vector[1]

            for j in range(1, len(knots)):
                follow = knots[j - 1]
                current = knots[j]
                tail_vector = get_tail_move((follow['r'], follow['c']), (current['r'], current['c']))
                current['r'] += tail_vector[0]
                current['c'] += tail_vector[1]
            positions.add((knots[-1]['r'], knots[-1]['c']))

    return positions


def part_one(lines: list[str]) -> int:
    return len(find_tail_positions(lines, 2))


def part_two(lines: list[str]) -> int:
    return len(find_tail_positions(lines, 10))


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
