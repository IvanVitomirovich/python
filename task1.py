def div_nums(x, y):
    if y == 0:
        return "Нельзя делить на ноль"
    else:
        return x / y


x = float(input('x: '))
y = float(input('x: '))
print(div_nums(x, y))

