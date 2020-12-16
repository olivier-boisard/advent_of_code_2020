import os
from collections import Counter


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
    persons_per_group = []
    persons_in_current_group = 0
    form = ''
    for line in data:
        if line == '':
            forms.append(form)
            persons_per_group.append(persons_in_current_group)
            persons_in_current_group = 0
            form = ''
        else:
            persons_in_current_group += 1
            form += line

    # Count answered questions
    counts = []
    for form, persons_in_current_group in zip(forms, persons_per_group):
        answers_cnts = Counter(form)
        cnt = 0
        for question in set(form):
            if answers_cnts[question] == persons_in_current_group:
                cnt += 1
        counts.append(cnt)

    print(sum(counts))


if __name__ == '__main__':
    main()
