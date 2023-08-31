def check(s, p, m):
    if s + p <= m:
        print('Вы можете позволить себе покупку')
    else:
        print('Вы не можете позволить себе покупку')

if __name__ == '__main__':
    s, p, m = input('Введите стоимость подписки, cтоимость пиццы и зарплату:').split()
    s, p, m = int(s), int(p), int(m)
    check(s, p, m)
