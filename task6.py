products = []
counter = 1
command = ''
while command != "stop":
    name = input('название: ')
    price = input('цена: ')
    amount = input('количество: ')
    units = input('eд: ')
    products.append(
        (counter, {"название": name, "цена": price, "количество": amount, "eд": units})
    )
    counter += 1
    command = input("Write 'stop' for stop inputting: ")
print(products)

result_dict = {
    "название": [],
    "цена": [],
    "количество": [],
    "eд": []
}

for numb, prod_dict in products:
    for key, value in prod_dict.items():
        result_dict[key].append(value)

print(result_dict)

