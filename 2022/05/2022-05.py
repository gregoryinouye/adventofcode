#!/usr/bin/env python3

import re
import sys
from collections import deque
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 'VJSFHWGFT'
part_two_answer = 'LCTQFBVZV'


def parse(input_path: Path) -> str:
    return input_path.read_text().rstrip()


def part_one(lines: str) -> str:
    crates, instructions = lines.split('\n\n')
    crates_split = crates.split('\n')

    crates_map = {}

    for crate_line in crates_split:
        crate_split = list(crate_line)
        for i, crate_char in enumerate(crate_split):
            if crate_char == ' ':
                continue
            elif crate_char == '[':
                continue
            elif crate_char == ']':
                continue
            elif crate_char.isdigit():
                break
            else:
                column = 1 + (i - 1) // 4
                crates_map[column] = crates_map.get(column, deque([]))
                crates_map[column].append(crate_char)

    instructions_split = instructions.split('\n')

    for instruction in instructions_split:
        pattern = re.compile(r'\d+')
        qty_to_move, from_stack, to_stack = pattern.findall(instruction)
        for i in range(int(qty_to_move)):
            crates_map[int(to_stack)].appendleft(crates_map[int(from_stack)].popleft())

    result = []
    for key, value in sorted(crates_map.items(), key=lambda kv: kv[0]):
        result.append(str(value.popleft()))

    return ''.join(result)


def part_two(lines: str) -> str:
    crates, instructions = lines.split('\n\n')
    crates_split = crates.split('\n')

    crates_map = {}

    for crate_line in crates_split:
        crate_split = list(crate_line)
        for i, crate_char in enumerate(crate_split):
            if crate_char == ' ':
                continue
            elif crate_char == '[':
                continue
            elif crate_char == ']':
                continue
            elif crate_char.isdigit():
                break
            else:
                column = 1 + (i - 1) // 4
                crates_map[column] = crates_map.get(column, deque([]))
                crates_map[column].append(crate_char)

    instructions_split = instructions.split('\n')

    for instruction in instructions_split:
        pattern = re.compile(r'\d+')
        qty_to_move, from_stack, to_stack = pattern.findall(instruction)
        move = []
        for i in range(int(qty_to_move)):
            move.append(crates_map[int(from_stack)].popleft())
        move.reverse()
        for crate in move:
            crates_map[int(to_stack)].appendleft(crate)

    result = []
    for key, value in sorted(crates_map.items(), key=lambda kv: kv[0]):
        result.append(str(value.popleft()))

    return ''.join(result)


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
