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
    func = {'*': lambda *x: prod(x), '+': lambda *x: sum(x)}
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

    elements = operation.split(' ')
    left_operand = elements[0]
    right_operand = elements[2]
    operator_str = elements[1]
    func_operator = func[operator_str]

    result = func_operator(int(left_operand), int(right_operand))
    if len(elements) > 3:
        operation_string = ' '.join([str(result)] + elements[3:])
        result = _compute(operation_string)
    return result


def _main():
    operations = _load_input()
    output = []
    for operation in operations:
        result = _compute(operation)
        output.append(result)
    print(sum(output))


if __name__ == '__main__':
    _main()
