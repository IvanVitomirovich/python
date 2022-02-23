def to_power(x, y):
    if x < 0:
        return 'X должен быть больше 0'
    if y > 0:
        return 'Y должен быть меньше 0'
    # return x ** y
    i = 1
    for em in range(y *- 1):
        i /= x
    return i


x = float(input('Введите положительное число x: '))
y = int(input('Введите отрицательную степень y: '))
print(to_power(x, y))

