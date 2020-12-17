import itertools
import os

RULES_NAME = 'rules'


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    data = {}
    with open(input_file_path, 'r') as f:
        current_key = RULES_NAME
        for line in f.readlines():
            stripped_lined = line.strip()
            if stripped_lined == '':
                current_key = None
            elif current_key is None:
                current_key = stripped_lined[:-1]
            elif current_key == RULES_NAME:
                if current_key not in data:
                    data[current_key] = {}
                split = stripped_lined.split(': ')
                ranges = []
                for ranges_str in split[1].split(' or '):
                    min_max = ranges_str.split('-')
                    ranges.append(range(int(min_max[0]), int(min_max[1]) + 1))
                data[current_key][split[0]] = list(itertools.chain(*ranges))
            elif current_key == 'your ticket':
                data[current_key] = _parse_ticket(stripped_lined)
            else:
                if current_key not in data:
                    data[current_key] = []
                data[current_key].append(_parse_ticket(stripped_lined))
    return data


def _parse_ticket(stripped_lines):
    return [int(value) for value in stripped_lines.split(',')]


def _main():
    data = _load_input()
    acceptable_numbers = set(itertools.chain(*data[RULES_NAME].values()))

    error_rate = 0
    for value in itertools.chain(*data['nearby tickets']):
        if value not in acceptable_numbers:
            error_rate += value
    print(error_rate)


if __name__ == '__main__':
    _main()
