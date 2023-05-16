import copy


def path(some_dict, some_key, current_path=''):
    for key, val in some_dict.items():
        simple_path = f"{current_path}.{key[4:]}" if current_path else key[4:]
        if key == some_key:
            return simple_path
        elif isinstance(val, dict):
            nested_path = path(val, some_key, simple_path)
            if nested_path is not None:
                return nested_path


def plain(inside):
    full_dict = copy.deepcopy(inside)
    same = copy.copy(inside)

    def inner(some_dict):
        result = []

        for key, val in some_dict.items():
            if isinstance(val, dict):
                if key[2:4] == '--':
                    result.append([f"Property '{path(full_dict, key)}' was updated. From [complex value] to {int_checker(some_dict[f'  ++{key[4:]}'])}"])
                elif key[2:4] == '++':
                    result.append([f"Property '{path(full_dict, key)}' was updated. From {int_checker(some_dict[f'  --{key[4:]}'])} to [complex value]"])
                else:
                    result.extend(inner(val))
            if key[2:4] == '- ':
                result.append([f"Property '{path(full_dict, key)}' was removed"])
            if key[2:4] == '+ ' and isinstance(val, dict):
                result.append([f"Property '{path(full_dict, key)}' was added with value: [complex value]"])
            if key[2:4] == '+ ' and not isinstance(val, dict):
                result.append([f"Property '{path(full_dict, key)}' was added with value: {int_checker(val)}"])
            if key[2:4] == '--' and not isinstance(val, dict):
                if not isinstance(some_dict[f'  ++{key[4:]}'], dict):
                    result.append([f"Property '{path(full_dict, key)}' was updated. From {int_checker(some_dict[f'  --{key[4:]}'])} to {int_checker(some_dict[f'  ++{key[4:]}'])}"])

        return result

    result_list = inner(same)
    lst_with_newlines = []
    for item in result_list:
        lst_with_newlines.extend(item)
    result_str = '\n'.join(lst_with_newlines)
    return result_str.replace("'None'", "null").replace("False", "false").replace("True", "true")


def int_checker(value):
    if isinstance(value, int):
        return value
    else:
        return f"'{value}'"
