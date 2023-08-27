class Field:
    def __init__(self, text):
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


class Number(Field):
    def __init__(self, text, number):
        super().__init__(text)
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


if __name__ == '__main__':
    text1 = Field('ggggg')
    num1 = Number('hhhhh', 2)
    print(text1.text)
    print(num1.text, num1.number)

    text1.text = 'dddd'
    num1.number = 4
    print(text1.text)
    print(num1.number)
    