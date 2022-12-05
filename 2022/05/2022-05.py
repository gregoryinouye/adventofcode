#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 'VJSFHWGFT'
part_two_answer = 'LCTQFBVZV'


def parse(input_path: Path) -> str:
    return input_path.read_text().rstrip()


def get_crates_and_instructions(lines: str) -> tuple[list[str], list[map]]:
    crates_raw, instructions_raw = lines.split('\n\n')
    crates_rows = crates_raw.split('\n')
    instructions_rows = instructions_raw.split('\n')

    crates = [row[1::4] for row in crates_rows if row[1].isdigit() is False]
    instructions = [map(int, row.split(' ')[1::2]) for row in instructions_rows]

    return crates, instructions


def build_stacks(crates: list[str]) -> dict[int, list[str]]:
    crates_map = {}
    reversed_crates = reversed(crates)

    for crate_row in reversed_crates:
        for i, crate_char in enumerate(crate_row):
            if crate_char != ' ':
                crates_map[i + 1] = crates_map.get(i + 1, [])
                crates_map[i + 1].append(crate_char)

    return crates_map


def part_one(lines: str) -> str:
    crates, instructions = get_crates_and_instructions(lines)
    crates_map = build_stacks(crates)

    for quantity, from_stack, to_stack in instructions:
        for i in range(quantity):
            crate = crates_map[from_stack].pop()
            crates_map[to_stack].append(crate)

    top_crates = (crates_map[key][-1] for key in range(1, len(crates_map) + 1))

    return ''.join(top_crates)


def part_two(lines: str) -> str:
    crates, instructions = get_crates_and_instructions(lines)
    crates_map = build_stacks(crates)

    for quantity, from_stack, to_stack in instructions:
        crates_to_move = crates_map[from_stack][-quantity:]
        del crates_map[from_stack][-quantity:]
        crates_map[to_stack].extend(crates_to_move)

    top_crates = (crates_map[key][-1] for key in range(1, len(crates_map) + 1))

    return ''.join(top_crates)


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
