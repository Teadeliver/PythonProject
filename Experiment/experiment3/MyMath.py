"""
编写程序， 创建类 My M ath ，计算圆的周长、面积和球的表面积和体积
并编写测试代码，结果均保留两位小数。 运行效果如下所示。
请输入半径：5
圆的周长=31.42
圆的面积=78.54
球的表面积=314.16
球的体积=523.60
"""

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
