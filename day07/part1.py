import os
from typing import List


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    with open(input_file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return data


def _bag_contains_target(bag_mapping, bag_color, target_color):
    contained_bags = bag_mapping[bag_color]
    if target_color in contained_bags:
        return True
    for contained_bag in contained_bags:
        if _bag_contains_target(bag_mapping, contained_bag, target_color):
            return True
    return False


def main():
    data = _load_input()

    # Parse rules
    bags = {}
    for rule in data:
        rule_split = rule.split(' bags contain ')
        container_color = rule_split[0]
        contained_colors = rule_split[1]

        contained_bags = []
        if 'no other' not in rule:
            contained_bags = [' '.join(contained.strip().split(' ')[1:3]) for contained in contained_colors.split(',')]
        bags[container_color] = contained_bags

    cnt = 0
    for color in bags.keys():
        if _bag_contains_target(bags, color, 'shiny gold'):
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
