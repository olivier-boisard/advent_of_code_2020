import os
from copy import copy
from typing import List


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def _run_program(instructions):
    instruction_index = 0
    acc = 0
    executed_instructions = []
    infinite_loop = False
    terminated = False
    while not infinite_loop and not terminated:
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

        infinite_loop = instruction_index in executed_instructions
        terminated = instruction_index >= len(instructions)
    return acc if terminated else None


def _main():
    instructions_original = _load_input()

    jmp_indices = [idx for idx in range(len(instructions_original)) if 'jmp' in instructions_original[idx]]
    nop_indices = [idx for idx in range(len(instructions_original)) if 'nop' in instructions_original[idx]]

    acc = None
    for idx in jmp_indices:
        instructions = copy(instructions_original)
        instructions[idx] = instructions[idx].replace('jmp', 'nop')
        acc = _run_program(instructions)
        if acc is not None:
            break

    if acc is None:
        for idx in nop_indices:
            instructions = copy(instructions_original)
            instructions[idx] = instructions[idx].replace('nop', 'jmp')
            acc = _run_program(instructions)
            if acc is not None:
                break
    print(acc)


if __name__ == '__main__':
    _main()
