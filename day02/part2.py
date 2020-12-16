import os


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = f.readlines()
    return data


def main():
    data = _load_input()

    # Check data validity
    for line in data:
        if len(line.split(':')) != 2:
            raise ValueError()

    # Process data
    n_compliant_passwords = 0
    for line in data:
        elements = line.split(': ')
        policy = elements[0]
        password = elements[1]

        # Parse policy
        policy_elements = policy.split(' ')
        one_based_indexes = policy_elements[0].split('-')
        first_letter = password[int(one_based_indexes[0]) - 1]
        second_letter = password[int(one_based_indexes[1]) - 1]
        letter = policy_elements[1]

        # Check policy complience
        if (letter == first_letter or letter == second_letter) and first_letter != second_letter:
            print(line, 'is compliant')
            n_compliant_passwords += 1
        else:
            print(line, 'not compliant')

    print('Number of compliant passwords:', n_compliant_passwords)


if __name__ == '__main__':
    main()
