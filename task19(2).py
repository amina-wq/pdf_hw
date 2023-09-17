def find_min_difference_number(numbers):
    numbers.sort()

    min_difference = float('inf')
    result_a, result_b = None, None

    for i in range(len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]
        if difference < min_difference:
            min_difference = difference
            result_a, result_b = numbers[i], numbers[i + 1]

    return result_a, result_b


if __name__ == "__main__":
    numbers = list(map(int, input("Enter the list of numbers: ").split()))
    print(find_min_difference_number(numbers))





