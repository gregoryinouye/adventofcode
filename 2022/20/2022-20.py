#!/usr/bin/env python3

from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 18257
part_two_answer = 4148032160983


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def move_value(moves: list[tuple[int, int]], move_order: int) -> list[tuple[int, int]]:
    length = len(moves)
    index = next(j for j in range(length) if moves[j][0] == move_order)
    move = moves[index][1]
    new_index = (index + move) % (length - 1)
    moves.insert(new_index, moves.pop(index))
    return moves


def part_one(lines: list[str]) -> int:
    moves = [(i, int(line)) for i, line in enumerate(lines)]
    length = len(moves)

    for i in range(len(moves)):
        moves = move_value(moves, i)

    index = next(i for i in range(length) if moves[i][1] == 0)
    coordinates = [moves[(index + i) % length] for i in [1000, 2000, 3000]]
    return sum(map(lambda v: v[1], coordinates))


def part_two(lines: list[str]) -> int:
    moves = [(i, int(line) * 811589153) for i, line in enumerate(lines)]
    length = len(moves)

    for _ in range(10):
        for i in range(len(moves)):
            moves = move_value(moves, i)

    index = next(i for i in range(length) if moves[i][1] == 0)
    coordinates = [moves[(index + i) % length] for i in [1000, 2000, 3000]]
    return sum(map(lambda v: v[1], coordinates))


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
