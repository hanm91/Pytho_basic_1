class DV:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DV(10,10)
print(div.divide_by_null(10, 10))
print(div.divide_by_null(100, 0))


