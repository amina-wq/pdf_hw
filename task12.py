def replace_words(string: str):
    return ' '.join(string.split()[::-1])


def count_words(string: str):
    return string.count(' ') + 1


def replace_year(string: str):
    return string.replace('2020', '2021')


if __name__ == '__main__':
    print(replace_words('Hello world'))
    print(count_words('Hello world'))
    print(replace_year('В 2020 году я буду все делать вовремя!'))