import os
from copy import copy


def _main():
    starting_numbers = [1, 20, 11, 6, 12, 0]
    numbers_record = {n: [i + 1] for i, n in enumerate(starting_numbers)}
    end_turn = 30000000

    last_spoken_number = starting_numbers[-1]
    for turn in range(len(starting_numbers) + 1, end_turn + 1):
        number_to_speak = 0
        records = numbers_record[last_spoken_number]
        if len(records) > 1:
            number_to_speak = turn - 1 - numbers_record[last_spoken_number][-2]
        if number_to_speak not in numbers_record:
            numbers_record[number_to_speak] = []
        numbers_record[number_to_speak].append(turn)
        last_spoken_number = number_to_speak
        if turn % 1000000 == 0:
            print(turn)
    print('At turn', turn, ':', last_spoken_number)


if __name__ == '__main__':
    _main()
