import json
from formatters.stylish import keys_recovery


def format_json(my_dict):
    data1 = json.dumps(keys_recovery(my_dict), indent=4)
    return data1
