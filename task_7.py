import json

companies = {}
proftbl_count, proftbl_sum = 0, 0
with open('text8.txt') as file:
    file_lines = file.readlines()

for line in file_lines:
    data = line.split()
    profit = float(data[2]) - float(data[3])
    companies.update({data[0]: profit})
    if profit > 0:
        proftbl_count += 1
        proftbl_sum += profit

average_profit = proftbl_sum / proftbl_count
result = [companies, {'Average profit excluding loss-making companies': average_profit}]

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)

with open('result.json', encoding='utf-8') as file:
    result = json.load(file)
    print(result)

