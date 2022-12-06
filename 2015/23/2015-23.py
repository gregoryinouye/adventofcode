#!/usr/bin/env python3

from enum import Enum, auto
from pathlib import Path
import sys
from typing import Optional

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 255
part_two_answer = 334


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


class Instruction(Enum):
    hlf = auto()
    inc = auto()
    jie = auto()
    jio = auto()
    jmp = auto()
    tpl = auto()


class Register(Enum):
    A = 'a'
    B = 'b'


def parse_instructions(lines: list[str]) -> list[tuple[Instruction, Register, int]]:
    instructions = []

    for line in lines:
        values = line.split(' ')
        command = Instruction[values[0]]
        register, offset = None, None

        match command:
            case Instruction.jmp:
                offset = int(values[1])
            case (Instruction.jie | Instruction.jio):
                register = Register(values[1].strip(','))
                offset = int(values[2])
            case Instruction():
                register = Register(values[1])
            case _:
                raise Exception(f'unknown command encountered: {command}')

        instructions.append((command, register, offset))

    return instructions


def process_jump(command: Instruction, register_value: Optional[int], offset: int) -> int:
    if (command == Instruction.jie and register_value % 2 == 1) or \
            (command == Instruction.jio and register_value != 1):
        return 1
    return offset


def compute_registers(instructions: list[tuple[Instruction, Register, int]], registers: dict[str, int]) -> dict[str, int]:
    i = 0

    while i < len(instructions):
        command, register, offset = instructions[i]

        match command:
            case Instruction.jmp | Instruction.jie | Instruction.jio:
                register_value = registers[register.value] if register else None
                i += process_jump(command=command, register_value=register_value, offset=offset)
                continue
            case Instruction.hlf:
                registers[register.value] //= 2
            case Instruction.inc:
                registers[register.value] += 1
            case Instruction.tpl:
                registers[register.value] *= 3
            case _:
                raise Exception('command not recognized')

        i += 1

    return registers


def part_one(lines: list[str]) -> int:
    instructions = parse_instructions(lines)
    registers = {'a': 0, 'b': 0}
    compute_registers(instructions, registers)
    return registers['b']


def part_two(lines: list[str]) -> int:
    instructions = parse_instructions(lines)
    registers = {'a': 1, 'b': 0}
    compute_registers(instructions, registers)
    return registers['b']


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
