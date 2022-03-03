with open('text2.txt') as file:
    file_lines = file.readlines()

staff = {}
sum_susalary = 0
for line in file_lines:
    staff_info = line.split()
    staff.update({staff_info[0]: float(staff_info[1])})
    sum_susalary += float(staff_info[1])
average_salary = sum_susalary / len(staff)
print(f'Средняя величина дохода сотрудников = {average_salary}')
print('Сотрудники имеющие оклад менее 20 тысяч')

for f, s in staff.items():
    if s < 20000:
        print(f'{f}: {s}')

