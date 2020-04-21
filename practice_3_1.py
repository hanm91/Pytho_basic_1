def my_func():
    """
    Возвращает частное от деления X на Y
    :param X:float
    :param Y:float
    :return: Результат вычисления

    """
    x = float(input('Введите Х '))
    y = float(input('Введите Y '))
    try:
        z = x/y
    except ZeroDivisionError:
        print ('Деление на 0 запрещено')
        return my_func()
    return x/y

var_1 = my_func()
print(var_1)