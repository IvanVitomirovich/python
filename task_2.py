sec = int(input('Введите время в секундах: '))
print(f'Время в формате чч:мм:сс  {sec // 3600:02}:{(sec % 3600) // 60:02}:{sec % 60:02}')
