def auth(login: str, password: str):
    if login == 'user' and password == 'qwerty':
        print('Authentication completed')
    else:
        print('Invalid login or password')


currencies = {
    'USD': 420,
    'EUR': 510,
    'RUB': 5.8,
}


def convert(currency, value):
    return currencies[currency] / value


if __name__ == '__main__':
    # AUTH
    login, password = input('Enter login and password: ').split()
    auth(login, password)

    # CURRENCIES
    try:
        amount = int(input('Insert amount in KZT: '))
        for idx, cur in enumerate(currencies, start=1):
            print(f'[{idx}] {cur}')

        idx = int(input('Choose currency: '))
        if idx > len(currencies):
            raise ValueError

        print(convert(list(currencies.keys())[idx - 1], amount))

    except Exception:
        print('Error')