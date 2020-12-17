import os
from copy import copy


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def _main():
    instructions = _load_input()
    memory = {}
    binary_string_len = 36
    mask = ['X'] * binary_string_len
    for instruction in instructions:
        split = instruction.split(' = ')
        target = split[0]
        arg = split[1]
        if target == 'mask':
            mask = arg
        else:
            address = int(target.split('[')[1][:-1])
            address_binary_string_before_mask = list(_binary_string_formatter(binary_string_len).format(address))
            address_binary_string_after_mask = []
            for m, v in zip(mask, address_binary_string_before_mask):
                address_binary_string_after_mask.append(v if m == '0' else m)

            floating_indices = [c == 'X' for c in address_binary_string_after_mask]
            n_floating = sum(floating_indices)
            addresses_to_write_to = []
            if n_floating == 0:
                addresses_to_write_to.append(''.join(address_binary_string_after_mask))
            else:
                x_indices = [i for i, x in enumerate(floating_indices) if x]
                for i in range(2 ** n_floating):
                    mask_values = _binary_string_formatter(n_floating).format(i)
                    assert len(mask_values) == len(x_indices)
                    for m, j in zip(mask_values, x_indices):
                        address_binary_string_after_mask[j] = m
                    addresses_to_write_to.append(''.join(address_binary_string_after_mask))

            for address_to_write_to in addresses_to_write_to:
                memory[address_to_write_to] = int(arg)

    print(sum(memory.values()))


def _binary_string_formatter(binary_string_len):
    return '{' + '0:0{}b'.format(binary_string_len) + '}'


if __name__ == '__main__':
    _main()
