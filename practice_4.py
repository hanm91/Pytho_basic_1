i = int(input('Введите положительное число \n'))
r = -1
if i>10:
    while i > 10:
        d = i % 10
        i //= 10
        if d > r:
            r = d
    print('Наибольшая цифра\n',r)
else:
    print('Наибольшая цифра\n',i)

