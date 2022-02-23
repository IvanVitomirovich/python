def sum_num(num_str, stop):
    num_list = num_str.split()
    sum_list = 0
    for em in num_list:
        if em == stop:
            break
        sum_list += int(em)

    return sum_list


stop_symbol = 's!'
print('Специальный символ для завершения программы - "s!"')
finish = False
i2 = 0
while not finish:
    num_str = input('Введите число через пробел: ')
    i2 += sum_num(num_str, stop_symbol)
    finish = stop_symbol in num_str
    print(f'Сумма: {i2}')

