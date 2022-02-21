number = int(input('Введите месяц в виде целого числа: '))
z, v, l, o = 'Зима', 'Весна', 'Лето', 'Осень'
my_dict = {
    12: z, 1: z, 2: z,
    3: v, 4: v, 5: v,
    6: l, 7: l, 8: l,
    9: o, 10: o, 11: o
}
print(my_dict[number])
