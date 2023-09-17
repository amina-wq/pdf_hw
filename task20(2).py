def balance_array(arr):
    sum_positive = sum(x for x in arr if x > 0)
    sum_negative = sum(x for x in arr if x < 0)

    abs_sum_negative = abs(sum_negative)

    if sum_positive == abs_sum_negative:
        return arr
    elif sum_positive > abs_sum_negative:
        diff = sum_positive - abs_sum_negative
        return arr + [diff]
    else:
        diff = abs_sum_negative - sum_positive
        return arr + [-diff]


if __name__ == "__main__":
    input_array = [-3, -2, 1, 2, 3, 4]
    result = balance_array(input_array)
    print(result)
