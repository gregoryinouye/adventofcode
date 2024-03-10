#!/usr/bin/env python3

import math
import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 23678
part_two_answer = 15455663


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')


def parse_card(card: str) -> list[set[int], set[int]]:
    card_number, all_numbers = card.split(':')
    winner_text, number_text = map(lambda x: x.strip(), all_numbers.split('|'))
    winners = set(map(int, winner_text.split()))
    numbers = set(map(int, number_text.split()))
    return [winners, numbers]


def count_winners(card: list[set[int], set[int]]) -> int:
    winners, numbers = card
    win_set = set(winners)
    number_set = set(numbers)
    return len(win_set.intersection(number_set))


def calculate_score(count: int) -> int:
    return math.floor(2 ** (count - 1))


def count_cards(winners: list[int]) -> int:
    copies = [1] * len(winners)
    for index, winner in enumerate(winners):
        for inner in range(index + 1, index + winner + 1):
            copies[inner] += copies[index]
    return sum(copies)


def part_one(lines: list[str]) -> int:
    cards = map(parse_card, lines)
    winners = map(count_winners, cards)
    scores = map(calculate_score, winners)
    return sum(scores)


def part_two(lines: list[str]) -> int:
    cards = map(parse_card, lines)
    winners = list(map(count_winners, cards))
    return count_cards(winners)


if __name__ == '__main__':
    paths = [test_filename] if len(sys.argv) <= 1 else sys.argv[1:]

    for path_str in paths:
        print(f"\n{path_str}:")
        puzzle_input = parse(Path(path_str))

        part_one_actual = part_one(puzzle_input)
        part_two_actual = part_two(puzzle_input)

        result_one = '\u2705 ' if part_one_actual == part_one_answer else '\u274c '
        result_two = '\u2705 ' if part_two_actual == part_two_answer else '\u274c '

        print(result_one, 'Part One:', part_one_actual)
        print(result_two, 'Part Two:', part_two_actual)
