#!/usr/bin/env python3

import itertools
import sys
from collections import namedtuple
from math import ceil
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 121
part_two_answer = 201


def parse(input_path: Path) -> str:
    return input_path.read_text().strip()


def get_boss_stats(lines: list[str]) -> tuple[int, int, int]:
    health, damage, armor = [int(line.split(': ')[1]) for line in lines]
    return health, damage, armor


Item = namedtuple('Item', 'name cost damage armor')

weapon_shop: list[Item] = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0),
]

armor_shop: list[Item] = [
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5),
    Item('No armor', 0, 0, 0),
]

ring_shop: list[Item] = [
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3),
    Item('No ring', 0, 0, 0),
    Item('No ring', 0, 0, 0),
]


def is_player_win(player: (int, int, int), boss: (int, int, int)):
    player_health, player_damage, player_armor = player
    boss_health, boss_damage, boss_armor = boss

    boss_damage_taken = max(1, player_damage - boss_armor)
    player_damage_taken = max(1, boss_damage - player_armor)

    boss_rounds = ceil(boss_health / boss_damage_taken)
    player_rounds = ceil(player_health / player_damage_taken)

    return boss_rounds <= player_rounds


def part_one(line: str) -> int:
    lines = line.split('\n')
    boss_stats = get_boss_stats(lines)

    min_cost = float('inf')
    for weapon in weapon_shop:
        for armor in armor_shop:
            for ring1, ring2 in itertools.combinations(ring_shop, 2):
                items = [weapon, armor, ring1, ring2]
                cost = sum(map(lambda item: item.cost, items))

                if min_cost < cost:
                    continue

                damage_stat = sum(map(lambda item: item.damage, items))
                armor_stat = sum(map(lambda item: item.armor, items))

                if is_player_win((100, damage_stat, armor_stat), boss_stats):
                    min_cost = min(min_cost, cost)

    return min_cost


def part_two(line: str) -> int:
    lines = line.split('\n')
    boss_stats = get_boss_stats(lines)

    max_cost = -1
    for weapon in weapon_shop:
        for armor in armor_shop:
            for ring1, ring2 in itertools.combinations(ring_shop, 2):
                items = [weapon, armor, ring1, ring2]
                cost = sum(map(lambda item: item.cost, items))

                if max_cost > cost:
                    continue

                damage_stat = sum(map(lambda item: item.damage, items))
                armor_stat = sum(map(lambda item: item.armor, items))

                if is_player_win((100, damage_stat, armor_stat), boss_stats) is False:
                    max_cost = max(max_cost, cost)

    return max_cost


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
