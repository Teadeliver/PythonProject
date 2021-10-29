import math


class MyMath:
    def __init__(self, r):
        self.r = r

    @staticmethod
    def perimeter():
        print('圆的周长 = {:.2f}'.format(2 * math.pi * r))

    @staticmethod
    def area():
        print('圆的面积 = {:.2f}'.format(math.pi * math.pow(r, 2)))

    @staticmethod
    def surface():
        print('球的表面积 = {:.2f}'.format(4 * math.pi * math.pow(r, 2)))

    @staticmethod
    def volume():
        print('球的体积 = {:.2f}'.format(4 / 3 * math.pi * math.pow(r, 3)))


r = input()

if r.isdigit():
    r = int(r)
    p1 = MyMath(r)
    p1.perimeter()
    p1.area()
    p1.surface()
    p1.volume()
else:
    print('请输入数字！')
