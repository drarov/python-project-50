
def format_dict(my_dict):

    def inner(some_dict, indent=0):
        result = []
        for key, value in some_dict.items():
            if isinstance(value, dict):
                result.append('{}{}: {{'.format(' ' * indent, key))
                result.extend(inner(value, indent + 4))
                result.append('{}}}'.format(' ' * (indent + 4)))
            else:
                result.append('{}{}:{}{}'.format(' ' * indent, key, ' ' if value != '' else '', value))
        return result
    formatted_str = '{\n%s\n}' % ('\n'.join(inner(my_dict)))
    return formatted_str.replace("True", 'true').replace("False", 'false').replace("None", "null")


def keys_recovery(some_dict):
    new_dict = {}
    for key, val in some_dict.items():
        if isinstance(val, dict) and key[2:4] == '--' or key[2:4] == '++':
            if key[2:4] == '--':
                new_dict[f'  - {key[4:]}'] = val
            elif key[2:4] == '++':
                new_dict[f'  + {key[4:]}'] = val
        else:
            if isinstance(val, dict):
                new_dict[key] = keys_recovery(some_dict[key])
            if not isinstance(val, dict):
                if key[2:4] == '--':
                    new_dict[f'  - {key[4:]}'] = val
                elif key[2:4] == '++':
                    new_dict[f'  + {key[4:]}'] = val
                elif key[2:4] == '==':
                    new_dict[f'    {key[4:]}'] = val
                else:
                    new_dict[key] = val

    return new_dict
