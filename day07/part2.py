import os
from collections import Counter
from typing import List


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def _compute_n_contained_bags(bag_mapping, target_color):
    contained_bags = bag_mapping[target_color]
    output = sum(bag_mapping[target_color].values())
    for contained_bag in contained_bags:
        output += contained_bags[contained_bag] * _compute_n_contained_bags(bag_mapping, contained_bag)
    return output


def main():
    data = _load_input()

    # Parse rules
    bags = {}
    for rule in data:
        rule_split = rule.split(' bags contain ')
        container_color = rule_split[0]
        contained_colors = rule_split[1]

        contained_bags = Counter()
        if 'no other' not in rule:
            for contained in contained_colors.split(','):
                split = contained.strip().split(' ')
                occurences = int(split[0])
                contained_bags[' '.join(split[1:3])] = occurences
        bags[container_color] = contained_bags

    print(_compute_n_contained_bags(bags, 'shiny gold'))


if __name__ == '__main__':
    main()
