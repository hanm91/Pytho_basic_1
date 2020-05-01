class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула в право'

    def turn_left(self):
        return f'{self.name} повернуло в лево'

    def show_speed(self):
        return f'Сейчас скорость {self.name} составляет {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Сейчас скорость {self.name} составляет {self.speed}')
        if self.speed > 60:
            return f'Превышение скорости'
        else:
            return f'Скорость в норме'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Сейчас скорость {self.name} составляет {self.speed}')
        if self.speed > 40:
            return f'Превышение скорости'
        else:
            return f'Скорость в норме'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


ferrari = SportCar(200, 'Красная', 'ferriri', False)
volga = TownCar(60, 'Синий', 'Волга', False)
lada = WorkCar(80, 'Зленый', 'Lada', True)
kia = PoliceCar(210, 'Синий',  'КИА', True)
print(lada.turn_left())
print(f'Когда {ferrari.turn_right()}, {lada.stop()}')
print(ferrari.show_speed())
print(volga.show_speed())
print(kia.show_speed())