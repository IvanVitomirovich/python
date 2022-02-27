from functools import reduce

numb_list = [x for x in range(100, 1001, 2)]
print(reduce(lambda a, b: a * b, numb_list))

