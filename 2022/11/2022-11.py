#!/usr/bin/env python3

import math
import operator
from pathlib import Path
import sys
from typing import NamedTuple, Callable

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


class Monkey(NamedTuple):
    id: str
    items: list[int]
    operation: Callable[[int], int]
    divisor: int
    get_catch_id: Callable[[int], int]


def build_monkey(lines: list[str]) -> Monkey:
    monkey_id: str = ''
    items: list[int] = []
    operation: Callable[[int, int], int]
    operation_param: int = -1
    divisor: int = -1
    true_id: int = -1
    false_id: int = -1

    for line in lines:
        match line.strip().split(' '):
            case ['Monkey', value]:
                monkey_id = value.strip(':')
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

    return Monkey(
        id=monkey_id,
        items=items,
        operation=lambda item: operation(item, operation_param),
        divisor=divisor,
        get_catch_id=lambda item: true_id if item % divisor == 0 else false_id
    )


def part_one(lines: list[str]) -> int:
    monkeys = [build_monkey(line.split('\n')) for line in lines]
    count = {}

    for i in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                count[monkey.id] = count.get(monkey.id, 0) + 1
                item = monkey.operation(item)
                item //= 3
                catch_id = monkey.get_catch_id(item)
                monkeys[catch_id].items.append(item)
            monkey.items.clear()

    sorted_count = sorted(count.values())
    return sorted_count[-1] * sorted_count[-2]


def part_two(lines: list[str]) -> int:
    monkeys = [build_monkey(line.split('\n')) for line in lines]
    common_divisor = math.prod(monkey.divisor for monkey in monkeys)
    count = {}

    for i in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                count[monkey.id] = count.get(monkey.id, 0) + 1
                item = monkey.operation(item)
                item %= common_divisor
                catch_id = monkey.get_catch_id(item)
                monkeys[catch_id].items.append(item)
            monkey.items.clear()

    sorted_count = sorted(count.values())
    return sorted_count[-1] * sorted_count[-2]


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
