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
        elements = line.split(':')
        policy = elements[0]
        password = elements[1]

        # Parse policy
        policy_elements = policy.split(' ')
        min_max_occurences = policy_elements[0].split('-')
        min_occurences = int(min_max_occurences[0])
        max_occurences = int(min_max_occurences[1])
        letter = policy_elements[1]

        # Count expected letter in password
        cnt = 0
        for letter_in_password in password:
            if letter_in_password == letter:
                cnt += 1

        # Check policy complience
        if min_occurences <= cnt <= max_occurences:
            print(line, 'is compliant')
            n_compliant_passwords += 1
        else:
            print(line, 'not compliant')

    print('Number of compliant passwords:', n_compliant_passwords)


if __name__ == '__main__':
    main()
