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
    data_diff = np.diff(np.sort(([int(line) for line in _load_input()])))
    print(((data_diff == 1).sum() + 1) * ((data_diff == 3).sum() + 1))


if __name__ == '__main__':
    main()
