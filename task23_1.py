big_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    for key, value in kwargs.items():
        big_dict[key] = value
    return big_dict


if __name__ == '__main__':
    # 1
    print('Task 1\n=====================================')
    print(biggest_dict(hello='world', name='Амина'))
    print(biggest_dict(big='dict', nice='work'))

    # 2
    print('Task 2\n=====================================')
    initial_id = id(big_dict)

    keys = list(big_dict.keys())
    big_dict[keys[0]], big_dict[keys[-1]] = big_dict[keys[-1]], big_dict[keys[0]]
    big_dict.pop(keys[1])
    big_dict['new_key'] = 'new_value'
    print(big_dict)

    current_id = id(big_dict)
    print(f'{initial_id} = {current_id}')