import itertools
import os
from copy import copy, deepcopy


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    seats_layout = [list(line) for line in _load_input()]

    # Run simulation
    changed = True
    while changed:
        seats_layout_copy = deepcopy(seats_layout)
        changed = False
        for y in range(len(seats_layout)):
            for x in range(len(seats_layout[y])):
                n_occupied_seen_seats = 0
                for offset_y, offset_x in itertools.product(range(-1, 2), range(-1, 2)):
                    if offset_y == 0 and offset_x == 0:
                        continue

                    looked_position_y = y + offset_y
                    looked_position_x = x + offset_x
                    y_out_of_border = looked_position_y < 0 or looked_position_y >= len(seats_layout)
                    x_out_of_border = looked_position_x < 0 or looked_position_x >= len(seats_layout[y])
                    stop_looking = y_out_of_border or x_out_of_border
                    while not stop_looking:
                        seen_location = seats_layout[looked_position_y][looked_position_x]
                        looked_position_y += offset_y
                        looked_position_x += offset_x
                        y_out_of_border = looked_position_y < 0 or looked_position_y >= len(seats_layout)
                        x_out_of_border = looked_position_x < 0 or looked_position_x >= len(seats_layout[y])
                        if seen_location == '#':
                            n_occupied_seen_seats += 1
                        if y_out_of_border or x_out_of_border or seen_location != '.':
                            stop_looking = True
                position = seats_layout[y][x]
                if position == 'L' and n_occupied_seen_seats == 0:
                    seats_layout_copy[y][x] = '#'
                    changed = True
                elif position == '#' and n_occupied_seen_seats >= 5:
                    seats_layout_copy[y][x] = 'L'
                    changed = True
        seats_layout = seats_layout_copy

    # Count number of occupied seats
    print(len([position for position in list(itertools.chain(*seats_layout)) if position == '#']))


if __name__ == '__main__':
    main()
