from random import randint


class Matrix:
    def __init__(self, numb):
        self.numb = numb

    def __str__(self):
        s = ''
        for i in range(len(self.numb)):
            for j in range(len(self.numb[i])):
                s += f'{self.numb[i][j]:03} '
            s += '\n'
        return s

    def __add__(self, other):
        numb = [
            [self.numb[i][j] + other.numb[i][j] for j in range(len(self.numb[i]))]
                for i in range(len(self.numb))]
        return Matrix(numb)


a = Matrix([[randint(0, 99) for _ in range(10)] for _ in range(10)])
b = Matrix([[randint(0, 99) for _ in range(10)] for _ in range(10)])
print(a)
print(b)
print(a + b)
