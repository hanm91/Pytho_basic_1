from itertools import cycle
from itertools import count
from time import sleep

for el in count(0): # бесконечный цикл
    print(el)
    sleep(1)


с = [1, 2 , 3 , 'Привет']
for el in cycle(с):  # бесконечный цикл
    print(el)
    sleep(1)
