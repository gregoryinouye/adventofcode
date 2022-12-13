#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 654
part_two_answer = 57


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def find_combinations(jars: list[int], target: int) -> list[list[int]]:
    solutions = []

    def dfs(sizes: list[int], index: int):
        if sum(sizes) == target:
            solutions.append(sizes.copy())
            return
        if sum(sizes) > target or index == len(jars):
            return

        sizes.append(jars[index])
        dfs(sizes=sizes, index=index + 1)

        sizes.pop()
        dfs(sizes=sizes, index=index + 1)

    dfs(sizes=[], index=0)
    return solutions


def part_one(lines: list[str], target: int = 150) -> int:
    jars = [int(line) for line in lines]
    solutions = find_combinations(jars=jars, target=target)
    return len(solutions)


def part_two(lines: list[str], target: int = 150) -> int:
    jars = [int(line) for line in lines]
    solutions = sorted(find_combinations(jars=jars, target=target), key=lambda sizes: len(sizes))
    return len(list(filter(lambda solution: len(solution) == len(solutions[0]), solutions)))


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
