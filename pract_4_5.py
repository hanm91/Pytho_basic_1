from functools import reduce

b = [itm for itm in range(100, 1001) if itm%2 == 0]

print(reduce(lambda x, y: x*y, b))
