def user_data(first_name, last_name, year, city, email, phone):
    return f'{first_name} {last_name} {year} {city} {email} {phone}'


fn = input("Имя: ")
ln = input("Фамилия: ")
y = input("Год рождения: ")
c = input("Город проживания: ")
e = input("Email: ")
p = input("Телефон: ")
print(user_data(first_name = fn, last_name = ln, year = y, city = c, email = e, phone = p))

