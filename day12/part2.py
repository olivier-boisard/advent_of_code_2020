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

    ship_position = complex(0, 0)  # absolute
    waypoint_position = complex(10, 1)  # relative to the ship
    for instruction in instructions:
        action = instruction[0]
        arg = int(instruction[1:])

        if action == 'N':
            waypoint_position += complex(0, 1) * arg
        elif action == 'S':
            waypoint_position += complex(0, -1) * arg
        elif action == 'E':
            waypoint_position += complex(1, 0) * arg
        elif action == 'W':
            waypoint_position += complex(-1, 0) * arg
        elif action == 'L':
            waypoint_position *= cmath.rect(1, np.deg2rad(arg))
        elif action == 'R':
            waypoint_position *= cmath.rect(1, -np.deg2rad(arg))
        elif action == 'F':
            ship_position += arg * waypoint_position
        else:
            raise RuntimeError()

    print(np.round(abs(ship_position.real)) + np.round(abs(ship_position.imag)))


if __name__ == '__main__':
    main()
