a = float(input('Введите параметр а '))
b = float(input('Введите параметр b '))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)