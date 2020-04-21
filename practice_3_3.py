def my_func(x:float, y:float, z:float) -> float:
    """
    Принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

    """
    by_list = [x, y, z]
    total = []
    a = by_list.pop(by_list.index(max(by_list)))
    total.append(a)
    b = by_list.pop(by_list.index(max(by_list)))
    total.append(b)
    c = sum(total)
    return c

print (my_func(5, 69, 7))

