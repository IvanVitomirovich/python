from itertools import cycle, count

n = 100
numb_list = [x for x in range(4)]
counter = count()
cycler = cycle(numb_list)
print([next(counter) for x in range(n)])
print([next(cycler) for x in range(n)])

