import itertools
import os

RULES_NAME = 'rules'


def _load_input():
    folder = os.path.dirname(__file__)
    input_file_path = os.path.join(folder, 'input.txt')
    data = {}
    with open(input_file_path, 'r') as f:
        current_key = RULES_NAME
        for line in f.readlines():
            stripped_lined = line.strip()
            if stripped_lined == '':
                current_key = None
            elif current_key is None:
                current_key = stripped_lined[:-1]
            elif current_key == RULES_NAME:
                if current_key not in data:
                    data[current_key] = {}
                split = stripped_lined.split(': ')
                ranges = []
                for ranges_str in split[1].split(' or '):
                    min_max = ranges_str.split('-')
                    ranges.append(range(int(min_max[0]), int(min_max[1]) + 1))
                data[current_key][split[0]] = list(itertools.chain(*ranges))
            elif current_key == 'your ticket':
                data[current_key] = _parse_ticket(stripped_lined)
            else:
                if current_key not in data:
                    data[current_key] = []
                data[current_key].append(_parse_ticket(stripped_lined))
    return data


def _parse_ticket(stripped_lines):
    return [int(value) for value in stripped_lines.split(',')]


def _main():
    data = _load_input()
    rules = data[RULES_NAME]
    acceptable_numbers = set(itertools.chain(*rules.values()))
    # Discard invalid tickets
    accepted_tickets = []
    for ticket in data['nearby tickets']:
        ticket_accepted = True
        for value in ticket:
            if value not in acceptable_numbers:
                ticket_accepted = False
                break
        if ticket_accepted:
            accepted_tickets.append(ticket)

    field_names = rules.keys()
    field_potential_positions = {field_name: set(range(len(field_names))) for field_name in field_names}

    # Find out what's what
    for ticket in accepted_tickets:
        for position, value in enumerate(ticket):
            for key, acceptable_values in rules.items():
                if value not in acceptable_values:
                    field_potential_positions[key] -= {position}

    unfound_fields = _retrieve_unfound_fields(field_potential_positions)
    while len(unfound_fields) > 0:
        found_fields = set(field_potential_positions.keys()) - unfound_fields
        for field in found_fields:
            position = list(field_potential_positions[field])[0]
            for unfound_field in unfound_fields:
                field_potential_positions[unfound_field] -= {position}
        unfound_fields = _retrieve_unfound_fields(field_potential_positions)

    field_positions = {}
    for key in field_potential_positions:
        field_positions[key] = list(field_potential_positions[key])[0]

    # Extract output
    target_field_indices = [value for key, value in field_positions.items() if 'departure' in key]
    output = 1
    for index in target_field_indices:
        output *= data['your ticket'][index]

    print(output)


def _retrieve_unfound_fields(field_potential_positions):
    return {key for key, value in field_potential_positions.items() if len(value) > 1}


if __name__ == '__main__':
    _main()
