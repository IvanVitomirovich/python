input_list = input('Введите значения через пробел: ')
split_list = input_list.split()
len_list = len(split_list)
i = 0
while i < len_list - 1:
    split_list[i], split_list[i + 1] = split_list[i + 1], split_list[i] # Обмен значениями через кортежи
    i += 2
print(split_list)

