#!/usr/bin/env python3

import operator
import re
from collections import deque
from pathlib import Path
import sys
from typing import Callable, Optional

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
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


def modify_data_for_part_two(data: list[str]) -> list[str]:
    new_b = f'{part_one_answer} -> b'
    return [s if not re.match(r'\d+ -> b$', s) else new_b for s in data]


def parse_instruction(instruction: str) -> tuple[Optional[str], list[str], str]:
    wire_input, output_wire = instruction.split(' -> ')
    input_split: list[str] = wire_input.split(' ')
    command: Optional[str] = next((item for item in input_split if item.isupper()), None)
    input_wires: list[str] = [item for item in input_split if not item.isupper()]
    return command, input_wires, output_wire


def part_one(steps: list[str], result_wire: str) -> int:
    wires: dict[str, int] = {}
    wires_to_process: deque[tuple[Optional[str], list[str], str]]
    wires_to_process = deque(parse_instruction(instruction) for instruction in steps)

    while result_wire not in wires and wires_to_process:
        op, input_wires, output_wire = wires_to_process.popleft()
        input_values = [int(wire) if wire.isdigit() else wires.get(wire, -1) for wire in input_wires]

        # if an input wire's value is currently unknown, skip and replace on queue
        if -1 in input_values:
            wires_to_process.append((op, input_wires, output_wire))
            continue

        wires[output_wire] = input_values[0] if op is None else operations[op](*input_values)

    return wires[result_wire]


def part_two(steps: list[str], result_wire: str):
    modified_steps = modify_data_for_part_two(steps)
    return part_one(modified_steps, result_wire)


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f'\n{path_str}:')
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input, 'a')
        part_two_actual = part_two(puzzle_input, 'a')

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
