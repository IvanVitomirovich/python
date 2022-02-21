input_str = input('Введите строку из нескольких слов: ')
strk = input_str.split()
i = 1
for word in strk:
    print(f'№ {i} : {word[:10]}')
    i += 1

