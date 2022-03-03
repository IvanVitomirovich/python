result = {}
with open('text7.txt') as file:
    file_lines = file.readlines()

for line in file_lines:
    data = line.split()
    hours = 0
    for el in data[1:]:
        if el != '-':
            numb = '0'
            for i in el:
                if i.isdigit():
                    numb += i
                else:
                    break
            hours += int(numb)
    result.update({data[0].strip(':'): hours})
print(result)
