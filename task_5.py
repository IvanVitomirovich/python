import random

with open('text6.txt', 'w') as new_file:
    for el in range(10):
        new_file.write(f'{random.randint(0, 10)} ')

with open('text6.txt') as new_file:
    numb_str = new_file.read().split()
    sum = 0
    for numb in numb_str:
        sum += int(numb)

print(sum)

