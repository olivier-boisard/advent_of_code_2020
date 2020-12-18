import os
from math import prod
import re


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def _compute(operation):
    start_idx = 0
    while '(' in operation:
        for i, c in enumerate(operation):
            if c == '(':
                start_idx = i
            elif c == ')':
                sub_operation = operation[start_idx + 1:i]
                result = _compute(sub_operation)
                operation = operation.replace(f'({sub_operation})', str(result), 1)
                break

    while '+' in operation:
        addition = re.search('[0-9]* \+ [0-9]*', operation).group(0)
        elements = addition.split(' + ')
        operation = operation.replace(addition, str(int(elements[0]) + int(elements[1])))

    while '*' in operation:
        addition = re.search('[0-9]* \* [0-9]*', operation).group(0)
        elements = addition.split(' * ')
        operation = operation.replace(addition, str(int(elements[0]) * int(elements[1])))

    return int(operation)


def _main():
    operations = _load_input()
    output = []
    for operation in operations:
        output.append(_compute(operation))
    print(sum(output))


if __name__ == '__main__':
    _main()
