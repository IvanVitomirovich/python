import sys

if len(sys.argv) < 4:
    print(f'Введите данные (выработка в часах, ставка в час, премия): ')
else:
    v = float(sys.argv[1])
    s = float(sys.argv[2])
    p = float(sys.argv[3])
    print(v * s + p)
