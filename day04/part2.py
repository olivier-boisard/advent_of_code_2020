import os


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = _load_input()

    # Extract passports
    passports = []
    passport = ''
    for line in data:
        if line == '':
            passports.append(passport)
            passport = ''
        else:
            passport += ' ' + line

    # Check passports
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    n_valids = 0
    for passport in passports:
        found_fields = set()
        for field in passport.split(' '):
            field_key_values = field.split(':')
            if len(field_key_values) < 2:
                continue
            field_key = field_key_values[0]
            field_value = field_key_values[1]

            # Add field to found ones if valid
            if _is_valid(field_key, field_value):
                found_fields.add(field_key)

        if found_fields == required_fields:
            n_valids += 1
        print('Found fields:', found_fields, '-> valid:', n_valids)

    print('Valid passports:', n_valids)


def _is_valid(field_key, field_value):
    # Check field is valid
    valid = False
    if field_key == 'byr':
        valid = 1920 <= int(field_value) <= 2002
    elif field_key == 'iyr':
        valid = 2010 <= int(field_value) <= 2020
    elif field_key == 'eyr':
        valid = 2020 <= int(field_value) <= 2030
    elif field_key == 'hgt':
        if len(field_value) <= 2:
            valid = False
        else:
            unit = field_value[-2:]
            height = int(field_value[:-2])
            if unit == 'cm':
                valid = 150 <= height <= 193
            elif unit == 'in':
                valid = 59 <= height <= 76
    elif field_key == 'hcl':
        valid = field_value[0] == '#'
        if valid:
            for character in field_value[1:]:
                if character not in [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']:
                    valid = False
                    break
    elif field_key == 'ecl':
        valid = field_value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field_key == 'pid':
        valid = len(field_value) == 9
        if valid:
            for character in field_value:
                if character not in [str(i) for i in range(10)]:
                    valid = False
                    break
    return valid


if __name__ == '__main__':
    main()
