a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

b = [itm for i, itm in enumerate(a) if a[i] > a[i - 1] ]


print(b)