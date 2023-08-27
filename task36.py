def array_element(arr: list, index: int):
    try:
        value = arr[index]
        print(value)
    except IndexError:
        print("Индекс выходит за границы массива!")


arr1 = [10, 20, 30, 40, 50, 60]

if __name__ == '__main__':
    array_element(arr1, 3)
    array_element(arr1,20)
