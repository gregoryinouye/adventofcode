#!/usr/bin/env python3
import math
from pathlib import Path
import sys

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 11266889531
part_two_answer = 77387711


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_packages(lines: list[str]) -> list[int]:
    return sorted([int(line) for line in lines])


def pick_packages(packages: list[int], target: int) -> list[list[int]]:
    results = []
    max_length = float('inf')

    def dfs(selected: list[int], index: int) -> None:
        nonlocal max_length

        if sum(selected) == target:
            results.append(selected.copy())
            max_length = min(max_length, len(selected))
            return
        if max_length <= len(selected) or sum(selected) > target or index == len(packages):
            return

        selected.append(packages[index])
        dfs(selected, index + 1)

        selected.pop()
        dfs(selected, index + 1)

    dfs(selected=[], index=0)

    return results


def part_one(lines: list[str]) -> int:
    packages = parse_packages(lines)
    packages.sort(reverse=True)
    target_sum = sum(packages) // 3

    options = pick_packages(packages, target_sum)
    sorted_by_quantum_entanglement = sorted(options, key=lambda items: math.prod(items))

    return math.prod(sorted_by_quantum_entanglement[0])


def part_two(lines: list[str]) -> int:
    packages = parse_packages(lines)
    packages.sort(reverse=True)
    target_sum = sum(packages) // 4

    options = pick_packages(packages, target_sum)
    sorted_by_quantum_entanglement = sorted(options, key=lambda items: math.prod(items))

    return math.prod(sorted_by_quantum_entanglement[0])


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
