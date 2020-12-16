import os
from typing import List
import numpy as np


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = [int(line) for line in _load_input()]
    init = [1, 2, 4]
    suite = []
    for joltage in range(1, max(data) + 1):
        if joltage <= 3:
            suite.append(init[joltage - 1] if joltage in data else 0)
        else:
            suite.append(sum(suite[-3:]) if joltage in data else 0)
    print(suite[-1])


if __name__ == '__main__':
    main()
