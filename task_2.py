with open('text.txt') as file:
    file_lines = file.readlines()

count_str = 0
for numb, line in enumerate(file_lines):
    count_str += 1
    count_words = len(line.split())
    print(f'String №{numb + 1} - {count_words} words')
print(f'Total {count_str} words')

