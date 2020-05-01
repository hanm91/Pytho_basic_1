from time import sleep
from itertools import cycle

class TrafficLight:
    __color = ('красный', 'жёлтый', 'зелёный')

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1


traffic = TrafficLight()
traffic.running()

