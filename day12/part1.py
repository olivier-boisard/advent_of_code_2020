import cmath
import os
import numpy as np


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    instructions = _load_input()

    position = complex(0, 0)
    orientation = complex(1, 0)
    for instruction in instructions:
        action = instruction[0]
        arg = int(instruction[1:])

        if action == 'N':
            position += complex(0, 1) * arg
        elif action == 'S':
            position += complex(0, -1) * arg
        elif action == 'E':
            position += complex(1, 0) * arg
        elif action == 'W':
            position += complex(-1, 0) * arg
        elif action == 'F':
            position += orientation * arg
        elif action == 'L':
            orientation *= cmath.rect(1, np.deg2rad(arg))
        elif action == 'R':
            orientation *= cmath.rect(1, -np.deg2rad(arg))
        else:
            raise RuntimeError()

    print(int(abs(position.real)) + int(abs(position.imag)))


if __name__ == '__main__':
    main()
