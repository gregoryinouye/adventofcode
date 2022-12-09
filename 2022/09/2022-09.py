#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 5878
part_two_answer = 2405


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def get_tail_move(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    head_r, head_c = head
    tail_r, tail_c = tail

    if head_r == tail_r and abs(head_c - tail_c) > 1:
        return 0, 1 if head_c > tail_c else -1
    if head_c == tail_c and abs(head_r - tail_r) > 1:
        return 1 if head_r > tail_r else -1, 0
    if abs(head_c - tail_c) <= 1 and abs(head_r - tail_r) <= 1:
        return 0, 0

    return 1 if head_r > tail_r else -1, 1 if head_c > tail_c else -1


def part_one(lines: str) -> int:
    lines_split = lines.split('\n')
    positions = set()
    head = {'r': 0, 'c': 0}
    tail = {'r': 0, 'c': 0}

    for command in lines_split:
        direction, value = command.split(' ')
        num = int(value)

        vector = None
        match direction, num:
            case 'L', _:
                vector = 0, -1
            case 'R', _:
                vector = 0, 1
            case 'D', _:
                vector = 1, 0
            case 'U', _:
                vector = -1, 0

        for i in range(num):
            head['r'] += vector[0]
            head['c'] += vector[1]
            tail_vector = get_tail_move((head['r'], head['c']), (tail['r'], tail['c']))
            tail['r'] += tail_vector[0]
            tail['c'] += tail_vector[1]
            positions.add((tail['r'], tail['c']))

    return len(positions)


def part_two(lines: str) -> int:
    lines_split = lines.split('\n')
    positions = set()
    head = {'r': 0, 'c': 0}
    knots = [{'r': 0, 'c': 0} for _ in range(9)]

    for command in lines_split:
        direction, value = command.split(' ')
        num = int(value)

        vector = None
        match direction, num:
            case 'L', _:
                vector = 0, -1
            case 'R', _:
                vector = 0, 1
            case 'D', _:
                vector = 1, 0
            case 'U', _:
                vector = -1, 0

        for i in range(num):
            head['r'] += vector[0]
            head['c'] += vector[1]

            for i, knot in enumerate(knots):
                follow = knots[i - 1] if i != 0 else head
                current = knots[i]
                tail_vector = get_tail_move((follow['r'], follow['c']), (current['r'], current['c']))
                current['r'] += tail_vector[0]
                current['c'] += tail_vector[1]
            positions.add((knots[-1]['r'], knots[-1]['c']))

    return len(positions)


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
