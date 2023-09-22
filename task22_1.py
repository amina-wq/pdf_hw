from collections import Counter


def is_superset(first_set: set, second_set: set) -> None:
    if first_set > second_set:
        print(f'Объект {first_set} - чистое супермножество')
    elif second_set > first_set:
        print(f'Объект {second_set} - чистое супермножество')
    elif first_set == second_set:
        print('Множества равны')
    else:
        print('Супермножество не обнаружено')


def set_gen(number_list):
    result = set()
    for number, repetitions in Counter(number_list).items():
        result.add(number)
        if repetitions > 1:
            for rep in range(2, repetitions + 1):
                result.add(str(number) * rep)
    return sorted(result, key=lambda x: int(x[0]) if isinstance(x, str) else x)


if __name__ == '__main__':
    # 1
    print('Task 1\n=====================================')
    a = {1, 2, 3}
    b = {4}
    c = {1, 2}

    is_superset(a, a)
    is_superset(a, b)
    is_superset(a, c)

    # 3
    print('Task 3\n=====================================')
    print(set_gen([1, 2, 3, 4, 4, 4, 3, 2, 3, 4]))