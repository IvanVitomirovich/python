class Zero(Exception):

    def __init__(self, txt):
        self.txt = txt


def division_number(a, b):
    try:
        if b == 0:
            raise Zero("Деление на ноль недопустимо!")
        else:
            return a / b
    except Zero as err:
        return err


num_1 = int(input('Введите делимое: '))
num_2 = int(input('Введите делитель: '))

print(division_number(num_1, num_2))
