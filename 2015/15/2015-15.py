#!/usr/bin/env python3

import math
from pathlib import Path
import sys
from typing import NamedTuple

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 21367368
part_two_answer = 1766400


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


class Ingredient(NamedTuple):
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def parse_ingredient(ingredient: str) -> Ingredient:
    name, stats = ingredient.split(': ')
    capacity, durability, flavor, texture, calories = [int(stat.split(' ')[1]) for stat in stats.split(', ')]
    return Ingredient(
        name=name,
        capacity=capacity,
        durability=durability,
        flavor=flavor,
        texture=texture,
        calories=calories
    )


def score_cookie(ingredients: list[Ingredient], count: list[int]) -> int:
    stats_sum = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0,
    }

    for i, ingredient in enumerate(ingredients):
        num = count[i]
        for k, v in ingredient._asdict().items():
            if k == 'name' or k == 'calories':
                continue
            stats_sum[k] += v * num

    return math.prod(map(lambda n: max(0, n), stats_sum.values()))


def sum_calories(ingredients: list[Ingredient], count: list[int]) -> int:
    return sum(ingredient.calories * amount for ingredient, amount in zip(ingredients, count))


def get_max_cookie_score(ingredients: list[Ingredient], max_calories: int = None) -> int:
    max_score = -1

    def dfs(count: list[int], index: int):
        if max_calories is not None and sum_calories(ingredients=ingredients, count=count) > max_calories:
            return
        if sum(count) == 100:
            nonlocal max_score
            max_score = max(score_cookie(ingredients=ingredients, count=count), max_score)
            print(max_score, count)
            return
        if index == len(count):
            return

        count[index] += 1
        dfs(count=count, index=index)

        count[index] -= 1
        dfs(count=count, index=index + 1)

    dfs(count=[0 for _ in range(len(ingredients))], index=0)
    return max_score


def part_one(lines: list[str]) -> int:
    ingredients = [parse_ingredient(line) for line in lines]
    return get_max_cookie_score(ingredients=ingredients)


def part_two(lines: list[str]) -> int:
    ingredients = [parse_ingredient(line) for line in lines]
    return get_max_cookie_score(ingredients=ingredients, max_calories=500)


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
