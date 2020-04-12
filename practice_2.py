var_time_second = int(input('Введите время в секундах \n'))
h = var_time_second//3600
m = (var_time_second//60)%60
s = var_time_second%60
if h<10:
    h = str('0' + str(h))
else:
    h = str(h)
if m<10:
    m = str('0' + str(m))
else:
    m = str(m)
if s<10:
    s = str('0' + str(s))
else:
    s = str(s)
print(f'Время {h}:{m}:{s}')
