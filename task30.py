class Field:
    def __init__(self, text):
        self.text = text

    def change(self, value):
        self.text = value


class Number(Field):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def change(self, text, number):
        self.text = text
        self.number = number


if __name__ == '__main__':
    text1 = Field('ggggg')
    num1 = Number('hhhhh', 2)
    print(text1.text)
    print(num1.text, num1.number)

    text1.change('dddd')
    num1.change('eeee', 4)
    print(text1.text)
    print(num1.text, num1.number)