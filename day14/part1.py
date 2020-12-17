import os


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def _main():
    instructions = _load_input()
    memory = {}
    mask = ['X'] * 36
    for instruction in instructions:
        split = instruction.split(' = ')
        target = split[0]
        arg = split[1]
        if target == 'mask':
            mask = arg
        else:
            value_before_mask = list('{0:036b}'.format(int(arg)))
            value_after_mask = []
            for m, v in zip(mask, value_before_mask):
                value_after_mask.append(v if m == 'X' else m)
            memory[target] = int(''.join(value_after_mask), base=2)

    print(sum(memory.values()))


if __name__ == '__main__':
    _main()
