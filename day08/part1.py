import os
from typing import List


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    instructions = _load_input()

    instruction_index = 0
    acc = 0
    executed_instructions = []

    while instruction_index not in executed_instructions:
        executed_instructions.append(instruction_index)
        instruction_split = instructions[instruction_index].split(' ')
        func = instruction_split[0]
        arg = int(instruction_split[1])
        if func == 'acc':
            acc += arg
            instruction_index += 1
        elif func == 'jmp':
            instruction_index += arg
        elif func == 'nop':
            instruction_index += 1
    print(acc)


if __name__ == '__main__':
    main()
