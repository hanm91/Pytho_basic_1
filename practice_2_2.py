var_1 = int(input('Введите количество значений списка '))
print('Введите значения')

my_list = []

while len(my_list)<=var_1-1:
    a = input('-->> ')
    my_list.append(a)
print(my_list)

i = 0
while i < len(my_list) - 1:
    el = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = el
    i += 2
print(my_list)