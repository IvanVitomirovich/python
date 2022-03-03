with open('text.txt', 'w') as file:
    input_line = input('Text:\n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line = input('Text:\n')

