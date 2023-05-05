"""Comparing two flat json files."""

import json
import yaml


def file_opener(file_path):
    """Opening some json file."""
    with open(file_path, 'r') as file:
        if file_path[-4:] == 'json':
            return json.load(file)
        if file_path[-4:] == 'yaml' or file_path[-4:] == '.yml':
            return yaml.safe_load(file)


def generate_diff(path1, path2):
    """A main function which creates a comparison of two flat json files."""
    data1 = file_opener(path1)
    data2 = file_opener(path2)

    def inner(first_dict, second_dict):
        diff_dict = {}
        common = set(first_dict).intersection(set(second_dict))
        if common:
            for item in common:
                if isinstance(first_dict[item], dict) and isinstance(second_dict[item], dict):
                    diff_dict[f'    {item}'] = inner(first_dict[item], second_dict[item])
                else:
                    if first_dict[item] == second_dict[item]:
                        diff_dict[f'    {item}'] = first_dict[item]
                    else:
                        if item in first_dict:
                            diff_dict[f'  - {item}'] = first_dict[item]
                        if item in second_dict:
                            diff_dict[f'  + {item}'] = second_dict[item]
        leftovers = set(first_dict).symmetric_difference(set(second_dict))
        if leftovers:
            for item in leftovers:
                if item in first_dict:
                    diff_dict[f'  - {item}'] = first_dict[item]
                if item in second_dict:
                    diff_dict[f'  + {item}'] = second_dict[item]
        d_sorted = dict(sorted(diff_dict.items(), key=lambda x: (x[0][4:])))
        formated = '{\n' + '\n'.join(format_dict(d_sorted)).replace('False', 'false').replace('True', 'true') + '\n}'
        return formated
    return inner(data1, data2)


def format_dict(some_dict, indent=0):
    result = []
    for key, value in some_dict.items():
        if isinstance(value, dict):
            result.append('{}{}: {{'.format(' ' * indent, key))
            result.extend(format_dict(value, indent + 4))
            result.append('{}}}'.format(' ' * indent))
        else:
            result.append('{}{}: {}'.format(' ' * indent, key, value))

    return result