number = abs(int(input('Введите целое положительное число: ')))
biggest_num = 0
while number > 0:
    if number % 10 > biggest_num:
        biggest_num = number % 10
        if number == 9:
            break
    number //=10
print(f'Самая большая цифра в числе: {biggest_num}')
