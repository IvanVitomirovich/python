my_list = [7, 5, 3, 3, 2]
user_rating = int(input('Введите новый элемент рейтинга: '))
inserted = False
i = 0
for elem in my_list:
    if user_rating > elem:
        my_list.insert(i, user_rating)
        break
    i += 1
else:
    my_list.append(user_rating)

print(my_list)
