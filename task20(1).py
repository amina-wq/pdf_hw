def align_strings_with_stars(strings):
    max_length = max(len(s) for s in strings)

    aligned_strings = ['*' * (max_length - len(s)) + s for s in strings]

    return aligned_strings


if __name__ == "__main__":
    M = int(input("Enter the amount of strings: "))
    strings = []
    for i in range(M):
        string = input(f"Enter {i + 1} string: ")
        strings.append(string)

    aligned_strings = align_strings_with_stars(strings)
    for aligned_string in aligned_strings:
        print(aligned_string)
