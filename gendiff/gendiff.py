"""Comparing two flat json files."""

import json


def json_open(file_path):
    """Opening some json file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_diff(path1, path2):
    """A main function which creates a comparison of two flat json files."""
    data1 = json_open(path1)
    data2 = json_open(path2)
    difference1 = set(data1) - set(data2)
    difference2 = set(data2) - set(data1)
    common = set(data1).intersection(set(data2))
    diff_dict = {}
    if difference1:
        diff_dict.update({f'- {key}': data1[key] for key in difference1})
    if difference2:
        diff_dict.update({f'+ {key}': data2[key] for key in difference2})
    if common:
        for key in common:
            if data1[key] == data2[key]:
                diff_dict[f'  {key}'] = data1[key]
            if data1[key] != data2[key]:
                diff_dict[f'- {key}'] = data1[key]
                diff_dict[f'+ {key}'] = data2[key]
    d_sorted = dict(sorted(diff_dict.items(), key=lambda x: (x[0][2:])))
    return json.dumps(d_sorted, indent=2).replace(',', '').replace('"', '')
