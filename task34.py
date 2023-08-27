class Roman:
    roman_to_int = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
                    'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                    'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    int_to_roman = {value: key for key, value in roman_to_int.items()}

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
            self.roman = Roman.int_to_roman.get(value, None)
        elif isinstance(value, str):
            self.value = Roman.roman_to_int.get(value, 0)
            self.roman = value
        else:
            raise ValueError("Invalid input")

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        elif isinstance(other, int):
            return Roman(self.value + other)
        else:
            raise TypeError("Unsupported operation")

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        elif isinstance(other, int):
            return Roman(self.value - other)
        else:
            raise TypeError("Unsupported operation")

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        elif isinstance(other, int):
            return Roman(self.value * other)
        else:
            raise TypeError("Unsupported operation")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)
        elif isinstance(other, int):
            return Roman(self.value // other)
        else:
            raise TypeError("Unsupported operation")

    @staticmethod
    def to_roman(num):
        if num <= 0:
            raise ValueError("Value must be positive")
        result = ""
        for value, symbol in sorted(Roman.int_to_roman.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value
        return result

    @staticmethod
    def to_int(roman):
        result = 0
        prev_value = 0
        for symbol in reversed(roman):
            value = Roman.roman_to_int[symbol]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result


if __name__ == '__main__':
    num1 = Roman(10)
    num2 = Roman("V")
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * 3)
    print(num1 / 2)

    print(Roman.to_roman(15))
    print(Roman.to_int("XXI"))

