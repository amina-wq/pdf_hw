def is_triangle_exists(a, b, c):
    return a + b > c or a + c > b or b + c > a

def is_number_even(a):
    return a % 2 == 0

def is_sum_greater(a, b, c):
    return a + b > c

def is_number_greater(a, b):
    return a > b


if __name__ == '__main__':
    print(is_triangle_exists(6, 7, 8))
    print(is_triangle_exists(2, 3, 6))

    print(is_number_even(2))
    print(is_number_even(7))

    print(is_sum_greater(4, 5, 6))
    print(is_sum_greater(4, 5, 20))

    print(is_number_greater(4, 3))
    print(is_number_greater(4, 12))