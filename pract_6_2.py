

class Road:

    def asphalt(self, _length, _width, _weight, _thickness):
        m = (_length * _width * _weight * _thickness)/1000
        print (f'Для покрытия дорожного полотна длиной {_length}м, шириной {_width}м, массой {_weight}м'
               f' асфальта для толщины в 1см и толщиной в {_thickness}м, необходимо {m} тонн' )


a = Road()
a.asphalt(20,5000,25,0.05)