import os
from typing import List


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = [int(line) for line in _load_input()]
    start_idx = 0
    stop_idx = 0
    target_found = False
    window_sum = data[start_idx]
    target = 138879426
    while not target_found:
        if window_sum < target:
            stop_idx += 1
            window_sum += data[stop_idx]
        elif window_sum > target:
            window_sum -= data[start_idx]
            start_idx += 1
        else:
            target_found = True

    window = data[start_idx:stop_idx+1]
    print('Weakness:', min(window) + max(window))


if __name__ == '__main__':
    main()
