#!/usr/bin/env python3

import sys
from pathlib import Path

filepath = Path(__file__)
test_filename = filepath.stem + '.txt'
test_filepath = filepath.parent / test_filename
part_one_answer = 13682
part_two_answer = 12881


def parse(input_path: Path) -> list[str]:
    return input_path.read_text().strip().split('\n')



def get_move(letter: str) -> str:
    match letter:
        case ('A' | 'X'):
            return 'ROCK'
        case ('B' | 'Y'):
            return 'PAPER'
        case ('C' | 'Z'):
            return 'SCISSORS'
        case _:
            raise Exception('unknown strategy guide letter')


def get_move_score(move: str) -> int:
    if move == 'ROCK':
        return 1
    elif move == 'PAPER':
        return 2
    else:
        return 3


def get_turn_score(opponent, player) -> int:
    if opponent == player:
        return 3
    elif (opponent, player) in {('ROCK', 'PAPER'), ('PAPER', 'SCISSORS'), ('SCISSORS', 'ROCK')}:
        return 6
    else:
        return 0


def get_strategy_move(letter: str, opponent: str) -> str:
    options = ['ROCK', 'PAPER', 'SCISSORS']
    opponent_index = options.index(opponent)
    strategy_modifier = None

    if letter == 'X':
        strategy_modifier = 2
    if letter == 'Y':
        strategy_modifier = 0
    if letter == 'Z':
        strategy_modifier = 1

    player_index = (opponent_index + strategy_modifier) % 3
    return options[player_index]


def part_one(lines: list[str]) -> int:
    score = 0

    for line in lines:
        opponent, player = map(get_move, line.split(' '))
        score += get_turn_score(opponent, player) + get_move_score(player)

    return score


def part_two(lines: list[str]) -> int:
    score = 0

    for line in lines:
        opponent_strategy, player_strategy = line.split(' ')
        opponent = get_move(opponent_strategy)
        player = get_strategy_move(player_strategy, opponent)
        score += get_turn_score(opponent, player) + get_move_score(player)

    return score


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
