#!/usr/bin/env python3

import operator
from collections import deque
from pathlib import Path
import sys
from typing import Callable

filepath = Path(__file__)
test_filename = filepath.stem.split('_')[0] + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 16076
part_two_answer = 2797

operations: dict[str, Callable[..., int]] = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
    'NOT': lambda binary: int(binary ^ 0xFFFF),
}


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def part_one(steps: list[str], wire_of_interest: str) -> int:
    wires: dict[str, int] = {}
    wires_to_process: deque[tuple[str, str]] = deque([])

    for step in steps:
        wire_input, wire = step.split(' -> ')
        input_split = wire_input.split(' ')

        if len(input_split) == 1 and input_split[0].isdigit():
            wires[wire] = int(input_split[0])
        else:
            wires_to_process.append((input_split, wire))

    while wire_of_interest not in wires and wires_to_process:
        wire_input, wire = wires_to_process.popleft()
        op = None
        input_wires = set()

        if len(wire_input) == 1:
            assert wire_input[0].isdigit() is False
            input_wires.add(wire_input[0])

        if len(wire_input) == 2:
            op = wire_input[0]
            assert op == 'NOT'
            input_wires.add(wire_input[1])

        if len(wire_input) == 3:
            op = wire_input[1]
            input_wires.update(filter(lambda item: item.islower(), wire_input))

        if input_wires.issubset(wires.keys()):
            if op is None:
                wires[wire] = wires[input_wires.pop()]
            else:
                input_values = map(lambda x: int(x) if x.isdigit() else wires[x],
                                   filter(lambda item: not item.isupper(), wire_input))
                wires[wire] = operations[op](*input_values)
        else:
            wires_to_process.append((wire_input, wire))

    return wires[wire_of_interest]


part_two = part_one

if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f"\n{path_str}:")
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input, 'a')
        part_two_actual = part_two(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
