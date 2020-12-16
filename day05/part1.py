import os


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = _load_input()

    seat_ids = []
    for line in data:
        row_number = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        column_number = int(line[7:].replace('L', '0').replace('R', '1'), 2)
        seat_ids.append(row_number * 8 + column_number)
    print('Output:', max(seat_ids))


if __name__ == '__main__':
    main()
