import os


def main():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [int(line) for line in f.readlines()]

        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                for k in range(j + 1, len(data)):
                    if data[i] + data[j] + data[k] == 2020:
                        print(data[i] * data[j] * data[k])


if __name__ == '__main__':
    main()
