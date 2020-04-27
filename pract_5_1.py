with open('test_5_1.txt', 'w', encoding= 'utf-8') as f_obj:
    line = input('Введите данные \n')
    while line:
        f_obj.writelines(line + "\n")
        line = input('Введите данные \n')
        if not line:
            break