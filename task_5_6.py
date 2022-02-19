revenue = abs(int(input("Введите выручку фирмы: ")))
costs = abs(int(input("Введите издержки фирмы: ")))
profit = revenue - costs
if revenue > costs:
    print(f'Фирма работает с прибылью: {profit}')
    print(f'Рентабельность выручки составила: {profit / revenue * 100} %')
    staff = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль в расчете на одного сторудника сотавила: {profit / staff}')
elif revenue == costs:
    print('Фирма работает в ноль')
else:
    print(f'Фирма работает в убыток: {profit}')
