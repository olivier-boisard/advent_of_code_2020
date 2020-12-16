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
                n_occupied_adjacent_seats = 0
                for offset_y in range(-1, 2):
                    for offset_x in range(-1, 2):

                        no_offset = (offset_x == 0 and offset_y == 0)
                        adjacent_seat_y = y + offset_y
                        adjacent_seat_x = x + offset_x
                        y_out_of_border = adjacent_seat_y < 0 or adjacent_seat_y >= len(seats_layout)
                        x_out_of_border = adjacent_seat_x < 0 or adjacent_seat_x >= len(seats_layout[y])
                        if no_offset or y_out_of_border or x_out_of_border:
                            continue

                        if seats_layout[adjacent_seat_y][adjacent_seat_x] == '#':
                            n_occupied_adjacent_seats += 1
                position = seats_layout[y][x]
                if position == 'L' and n_occupied_adjacent_seats == 0:
                    seats_layout_copy[y][x] = '#'
                    changed = True
                elif position == '#' and n_occupied_adjacent_seats >= 4:
                    seats_layout_copy[y][x] = 'L'
                    changed = True
        seats_layout = seats_layout_copy

    # Count number of occupied seats
    print(len([position for position in list(itertools.chain(*seats_layout)) if position == '#']))


if __name__ == '__main__':
    main()
