#!/usr/bin/env python3

import math
import operator
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 78960
part_two_answer = 14561971968


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n\n')

operator_mapping = {
    '+': operator.add,
    '*': operator.mul,
    '**': operator.pow
}

def build_monkey(lines: list[str]) -> object:
    monkey_id: int = -1
    items: list[int] = []
    operation: str = ''
    operation_param: int = -1
    divisor: int = -1
    true_id: int = -1
    false_id: int = -1

    for line in lines:
        match line.strip().split(' '):
            case ['Monkey', value]:
                monkey_id = int(value.strip(':'))
            case ['Starting', 'items:', *numbers]:
                items.extend(map(lambda n: int(n.strip(',')), numbers))
            case ['Operation:', 'new', '=', 'old', op_string, value]:
                if value == 'old' and op_string == '*':
                    op_string = '**'
                    value = '2'
                operation = operator_mapping[op_string]
                operation_param = int(value)
            case ['Test:', 'divisible', 'by', value]:
                divisor = int(value)
            case ['If', bool_str, 'throw', 'to', 'monkey', value]:
                if bool_str.strip(':') == 'true':
                    true_id = int(value)
                else:
                    false_id = int(value)

    return {
        'id': monkey_id,
        'items': items,
        'operation': operation,
        'operation_value': operation_param,
        'divisor': divisor,
        'true_id': true_id,
        'false_id': false_id
    }

def part_one(lines: list[str]) -> int:
    monkeys = [build_monkey(line.split('\n')) for line in lines]
    count = [0 for _ in monkeys]
    for i in range(20):
        for monkey in monkeys:
            for item in monkey['items']:
                count[monkey['id']] += 1
                item = monkey['operation'](item, monkey['operation_value'])
                item //= 3
                destination_monkey_id = monkey['true_id'] if item % monkey['divisor'] == 0 else monkey['false_id']
                monkeys[destination_monkey_id]['items'].append(item)
            monkey['items'].clear()
    count.sort()
    return count[-1] * count[-2]


def part_two(lines: list[str]) -> int:
    monkeys = [build_monkey(line.split('\n')) for line in lines]
    common_divisor = math.prod(monkey['divisor'] for monkey in monkeys)
    count = [0 for _ in monkeys]
    for i in range(10000):
        for monkey in monkeys:
            for item in monkey['items']:
                count[monkey['id']] += 1
                item = monkey['operation'](item, monkey['operation_value'])
                item %= common_divisor
                destination_monkey_id = monkey['true_id'] if item % monkey['divisor'] == 0 else monkey['false_id']
                monkeys[destination_monkey_id]['items'].append(item)
            monkey['items'].clear()
    count.sort()
    return count[-1] * count[-2]


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
