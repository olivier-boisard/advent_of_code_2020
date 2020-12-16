import os


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def main():
    data = _load_input()

    # Extract forms
    forms = []
    form = ''
    for line in data:
        if line == '':
            forms.append(form)
            form = ''
        else:
            form += line

    # Count answered questions
    counts = []
    for form in forms:
        counts.append(len(set(form)))
        print(form)
    print(sum(counts))


if __name__ == '__main__':
    main()
