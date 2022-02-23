def int_func(letters): #6
    word = letters[0].upper() + letters[1:]
    return word


user_str = input('Введите слова через пробел: ') #7
for word in user_str.split():
    print(f'{int_func(word)} ', end='')

