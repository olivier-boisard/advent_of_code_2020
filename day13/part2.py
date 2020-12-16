import os
from functools import reduce


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'example.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


# Got from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    result = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        result += a_i * mul_inv(p, n_i) * p
    return result % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def main():
    data = _load_input()

    bus_loop_durations = [int(duration) for duration in data[1].split(',') if duration != 'x']
    bus_timestamp_offsets = [index for index, duration in enumerate(data[1].split(',')) if duration != 'x']

    print(chinese_remainder(bus_loop_durations, bus_timestamp_offsets))


if __name__ == '__main__':
    main()
