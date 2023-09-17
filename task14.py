def count_marks(marks_list: list):
    counter = {5: 0, 4: 0, 3: 0, 2: 0}
    for mark in marks_list:
        counter[mark] += 1
    return counter


def correct_bad_marks(marks_list: list):
    for i in range(len(marks_list)):
        if marks_list[i] == 2:
            marks_list[i] = 3
    return marks_list


if __name__ == '__main__':
    marks = input('Write your marks: ').strip().split(' ')
    try:
        marks = list(map(int, marks))
    except ValueError:
        print('Write your marks space-separated')

    print(*count_marks(marks).values(), sep=' ')
    print(sum(marks) / len(marks))

    print(*correct_bad_marks(marks))
