#!/usr/bin/env python3

import operator
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 21208142603224
part_two_answer = 3882224466191


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


operator_map = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

reverse_operator_map = {
    '+': operator.sub,
    '-': operator.add,
    '*': operator.floordiv,
    '/': operator.mul,
}


def parse_monkeys(lines: list[str], is_part_two: bool) -> tuple[dict[str, int], dict]:
    numbers = {}
    expressions = {}

    for line in lines:
        match line.split(' '):
            case ['humn:', _] if is_part_two:
                pass
            case [monkey, value] if value.isdecimal():
                numbers[monkey.strip(':')] = int(value)
            case ['root:', monkey_param1, '+', monkey_param2] if is_part_two:
                expressions['root'] = '=', monkey_param1, monkey_param2
            case [monkey, monkey_param1, op, monkey_param2]:
                expressions[monkey.strip(':')] = op, monkey_param1, monkey_param2
            case _:
                raise Exception(f'unexpected data format: {line}')

    return numbers, expressions


def part_one(lines: list[str]) -> int:
    numbers, expressions = parse_monkeys(lines=lines, is_part_two=False)

    while 'root' not in numbers:
        for monkey, expression in list(expressions.items()):
            if expression[1] not in numbers or expression[2] not in numbers:
                continue
            numbers[monkey] = operator_map[expression[0]](numbers[expression[1]], numbers[expression[2]])
            del expressions[monkey]

    return numbers['root']


def part_two(lines: list[str]) -> int:
    numbers, expressions = parse_monkeys(lines=lines, is_part_two=True)
    reverse_evaluate = None

    while 'humn' not in numbers:
        for monkey, expression in list(expressions.items()):
            if monkey == 'root':
                if expression[1] in numbers:
                    numbers[expression[2]] = numbers[expression[1]]
                    del expressions[monkey]
                    reverse_evaluate = expression[2]
                elif expression[2] in numbers:
                    numbers[expression[1]] = numbers[expression[2]]
                    del expressions[monkey]
                    reverse_evaluate = expression[1]
            elif reverse_evaluate == monkey:
                if expression[1] in numbers:
                    if expression[0] == '/' or expression[0] == '-':
                        numbers[expression[2]] = operator_map[expression[0]](numbers[expression[1]], numbers[monkey])
                    else: # '*' or '+'
                        numbers[expression[2]] = reverse_operator_map[expression[0]](numbers[monkey], numbers[expression[1]])
                    del expressions[monkey]
                    reverse_evaluate = expression[2]
                elif expression[2] in numbers:
                    numbers[expression[1]] = reverse_operator_map[expression[0]](numbers[monkey], numbers[expression[2]])
                    del expressions[monkey]
                    reverse_evaluate = expression[1]
            elif expression[1] not in numbers or expression[2] not in numbers:
                continue
            else:
                numbers[monkey] = operator_map[expression[0]](numbers[expression[1]], numbers[expression[2]])
                del expressions[monkey]

    return numbers['humn']


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
