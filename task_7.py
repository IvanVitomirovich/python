a = float(input('Введите результаты пробежки первого дня в км: '))
b = float(input('Введите общий желаемый результат в км: '))
result_days = 1
while a < b:
        a *= 1.1
        result_days += 1
print(f'Вы достигнете требуемых показателей на {result_days} день')
