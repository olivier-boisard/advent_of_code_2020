import itertools
import os
from copy import copy


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def _main():
    data = _load_input()

    # Get active cubes' coordinates
    active_cubes = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                active_cubes.add((i, j, 0, 0))

    n_cycles = 6
    for _ in range(n_cycles):
        # Compute space boundaries
        x_min = min([active_cube[0] for active_cube in active_cubes]) - 1
        y_min = min([active_cube[1] for active_cube in active_cubes]) - 1
        z_min = min([active_cube[2] for active_cube in active_cubes]) - 1
        w_min = min([active_cube[3] for active_cube in active_cubes]) - 1
        x_max = max([active_cube[0] for active_cube in active_cubes]) + 1
        y_max = max([active_cube[1] for active_cube in active_cubes]) + 1
        z_max = max([active_cube[2] for active_cube in active_cubes]) + 1
        w_max = max([active_cube[3] for active_cube in active_cubes]) + 1

        active_cubes_copy = copy(active_cubes)
        iterator = itertools.product(
            range(x_min, x_max + 1),
            range(y_min, y_max + 1),
            range(z_min, z_max + 1),
            range(w_min, w_max + 1),
        )
        for x, y, z, w in iterator:
            # Get number of active neighbours
            neighbours_relative_coordinates = set(itertools.product(*[range(-1, 2)] * 4)) - {(0, 0, 0, 0)}
            active_neighbours_cnt = 0
            for x_prime, y_prime, z_prime, w_prime in neighbours_relative_coordinates:
                if (x + x_prime, y + y_prime, z + z_prime, w + w_prime) in active_cubes:
                    active_neighbours_cnt += 1

            current_cube_coordinates = (x, y, z, w)
            current_cube_is_active = current_cube_coordinates in active_cubes
            if current_cube_is_active and not (active_neighbours_cnt == 2 or active_neighbours_cnt == 3):
                active_cubes_copy -= {current_cube_coordinates}
            elif not current_cube_is_active and active_neighbours_cnt == 3:
                active_cubes_copy.update({current_cube_coordinates})
        active_cubes = active_cubes_copy

    print(len(active_cubes))


if __name__ == '__main__':
    _main()
