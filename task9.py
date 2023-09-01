def find_lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm


if __name__ == '__main__':
    a = int(input('Enter the number of members in team a: '))
    b = int(input('Enter the number of members in team b: '))
    print(f"LCM = {find_lcm(a,b)}")
