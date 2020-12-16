import cmath
import os
import numpy as np
import numpy as np


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = _load_input()

    arrival_timestamp = int(data[0])
    bus_loop_durations = [int(duration) for duration in data[1].split(',') if duration != 'x']

    rests = np.array([-arrival_timestamp % bus_loop_duration for bus_loop_duration in bus_loop_durations])
    min_waiting_time_idx = rests.argmin()
    earliest_bus_loop_duration = bus_loop_durations[min_waiting_time_idx]
    bus_arrival_time = ((arrival_timestamp // earliest_bus_loop_duration) + 1) * earliest_bus_loop_duration
    earliest_bus_waiting_time = bus_arrival_time - arrival_timestamp

    print(earliest_bus_loop_duration * earliest_bus_waiting_time)


if __name__ == '__main__':
    main()
