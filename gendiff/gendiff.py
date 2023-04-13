import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1:
        data1 = json.load(file1)
    with open(file_path2, 'r') as file2:
        data2 = json.load(file2)
    set1 = set(data1)
    set2 = set(data2)
    set_difference1 = set1 - set2
    set_difference2 = set2 - set1
    set_intersection = set1.intersection(set2)
    diff_dict = {}
    if set_difference1:
        dif_dict1 = {f'- {key}': data1[key] for key in set_difference1}
        diff_dict.update(dif_dict1)
    if set_difference2:
        dif_dict2 = {f'+ {key}': data2[key] for key in set_difference2}
        diff_dict.update(dif_dict2)
    if set_intersection:
        inter_dict1 = {f'  {key}': data1[key] for key in set_intersection if data1[key] == data2[key]}
        inter_dict2 = {f'- {key}': data1[key] for key in set_intersection if data1[key] != data2[key]}
        inter_dict3 = {f'+ {key}': data2[key] for key in set_intersection if data1[key] != data2[key]}
        diff_dict.update(inter_dict1)
        diff_dict.update(inter_dict2)
        diff_dict.update(inter_dict3)

    diff_dict_sorted = dict(sorted(diff_dict.items(), key=lambda x: (x[0][2:])))
    output_dict = json.dumps(diff_dict_sorted, indent=2).replace(',', '').replace('"', '')
    return output_dict
