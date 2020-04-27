with open('test_5_5.txt', 'w', encoding= 'utf-8') as f_obj:
    line = input('Введите цифры через пробел \n')
    f_obj.writelines(line)
    numb_1 = line.split()

result = [int(item) for item in numb_1]
print(f'Сумма введенных чисел равна {sum(result)}')

