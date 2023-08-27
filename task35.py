def plus_two(number: int):
    try:
        result = 2 + number
        print(result)
    except TypeError:
        print('Ожидаемый тип данных — число!')


if __name__ == '__main__':
    plus_two(5)
    plus_two('ddd')