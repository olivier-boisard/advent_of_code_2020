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
            field_key = field.split(':')[0]
            if field_key in required_fields:
                found_fields.add(field_key)
        valid = found_fields == required_fields
        if valid:
            n_valids += 1
        print('Found fields:', found_fields, '-> valid:', valid)

    print('Valid passports:', n_valids)


if __name__ == '__main__':
    main()
