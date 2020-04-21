def my_func(x: int, y: int) -> int:
    """
    Принимает два аргумента х и у и возвращает х в степени у.

    """
    c = x**y
    return c

print (my_func(2, 6))

def my_func2 (x:int, y:int) -> int:
    """
    Принимает два аргумента х и у и возвращает х в степени у.

    """
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print (my_func2(2, 2))