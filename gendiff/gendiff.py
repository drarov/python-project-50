"""Comparing two flat json files."""

import json
import yaml
from formatters.plain import plain
from formatters.stylish import keys_recovery, format_dict


def file_opener(file_path):
    """Opening some json file."""
    with open(file_path, 'r') as file:
        if file_path[-4:] == 'json':
            return json.load(file)
        if file_path[-4:] == 'yaml' or file_path[-4:] == '.yml':
            return yaml.safe_load(file)


def generate_diff(path1, path2, format_name='stylish'):
    """A main function which creates a comparison of two flat json files."""
    data1 = prepare(file_opener(path1))
    data2 = prepare(file_opener(path2))
    diff = structure(data1, data2)
    if format_name == 'stylish':
        return format_dict(keys_recovery(diff))
    elif format_name == 'plain':
        return plain(diff)
    else:
        return '"format_name" is not applicable, put the valid format name'


def structure(first_dict, second_dict):
    diff_dict = {}
    common = set(first_dict).intersection(set(second_dict))
    if common:
        for item in common:
            if isinstance(first_dict[item], dict) and isinstance(second_dict[item], dict):
                diff_dict[f'{item}'] = structure(first_dict[item], second_dict[item])
            else:
                if first_dict[item] == second_dict[item]:
                    diff_dict[f'  =={item[4:]}'] = first_dict[item]
                else:
                    if item in first_dict:
                        diff_dict[f'  --{item[4:]}'] = first_dict[item]
                    if item in second_dict:
                        diff_dict[f'  ++{item[4:]}'] = second_dict[item]
    leftovers = set(first_dict).symmetric_difference(set(second_dict))
    if leftovers:
        for item in leftovers:
            if item in first_dict:
                diff_dict[f'  - {item[4:]}'] = first_dict[item]
            if item in second_dict:
                diff_dict[f'  + {item[4:]}'] = second_dict[item]
    d_sorted = dict(sorted(diff_dict.items(), key=lambda x: (x[0][4:])))
    return d_sorted


def prepare(some_dict):
    prepared = {}
    for key, val in some_dict.items():
        if isinstance(val, dict):
            prepared[f'    {key}'] = prepare(val)
        else:
            prepared[f'    {key}'] = val
    return prepared
