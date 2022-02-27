def fact(number):
    cur = 1
    for i in range(1, number + 1):
        cur *= i
        yield cur


n = 10
for index, el in enumerate(fact(n)):
    print(f'№{index + 1} {el}')

