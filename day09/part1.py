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
    window_start_idx = 0
    window_stop_idx = window_start_idx + 25
    incorrect_value = None
    while window_stop_idx < len(data):
        window = sorted(data[window_start_idx:window_stop_idx])
        current_value = data[window_stop_idx]
        found_sum = False
        for i in range(len(window)):
            for j in range(i + 1, len(window)):
                a = window[i]
                b = window[j]
                if a != b and (a + b == current_value):
                    found_sum = True
                    break
                elif a + b > current_value:
                    break
            if found_sum or 2 * window[i] > current_value:
                break
        if not found_sum:
            incorrect_value = current_value
            break
        window_start_idx += 1
        window_stop_idx += 1

    print(incorrect_value)


if __name__ == '__main__':
    main()
