import os
import numpy as np


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = _load_input()

    drifts = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    output = 1
    for right_drift, down_drift in drifts:
        coordinates = {'x': 0, 'y': 0}
        cnt = 0
        while coordinates['y'] < len(data):
            x_shifted = coordinates['x'] % len(data[coordinates['y']])
            if data[coordinates['y']][x_shifted] == '#':
                cnt += 1
            coordinates = {'x': coordinates['x'] + right_drift, 'y': coordinates['y'] + down_drift}
        output *= cnt

    print('Multiplication:', output)


if __name__ == '__main__':
    main()
