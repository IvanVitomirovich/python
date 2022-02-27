numb_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [numb_list[i] for i in range(1, len(numb_list)) if numb_list[i] > numb_list[i - 1]]
print(result)

