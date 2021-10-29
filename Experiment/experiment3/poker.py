"""编写程序， 4 名牌手打牌，计算机随机将 52 张牌（不含大小鬼）发给
4 名牌手，在屏幕上显示每位牌手的牌。 创建函数 gen_pocker() 交换牌
的顺序，函数 get Color( 获取牌的花色，函数 get Value() 获取牌的牌
面大小，函数
面大小，函数getgetPuk()Puk()获取花获取花色和牌面大小的组合色和牌面大小的组合
提示：
提示：将要发的将要发的5252张牌，按照梅花张牌，按照梅花00……1212，方块，方块1313……2525，红桃，红桃2626……3838，，黑桃黑桃3939……5151顺序编号并存储在顺序编号并存储在pockerpocker列表（未洗牌之前）。也就是说列表（未洗牌之前）。也就是说列表某元素存储是列表某元素存储是1414则说明是方块则说明是方块22，，2626则说明是红桃则说明是红桃AA。。gen_pocker(n)gen_pocker(n)随机产生两个位置索引，交换两个位置的牌，进行随机产生两个位置索引，交换两个位置的牌，进行100100次随机交换两张次随机交换两张牌，从而达到洗牌目的。发牌时，将交换后牌，从而达到洗牌目的。发牌时，将交换后pockerpocker列表，按照顺序加列表，按照顺序加到到44个牌手的列表中。个牌手的列表中。
运行效果如下所示。
运行效果如下所示。
[51, 45, 31, 4, 48, 26, 11, 2, 24, 44, 22, 21,
[51, 45, 31, 4, 48, 26, 11, 2, 24, 44, 22, 21, 16, 41, 50, 47, 16, 41, 50, 47, 13, 25, 17, 29, 42, 27, 19, 33, 5, 40, 1, 8, 30, 18, 10, 9, 0, 13, 25, 17, 29, 42, 27, 19, 33, 5, 40, 1, 8, 30, 18, 10, 9, 0, 3, 14, 46, 36, 35, 12, 15, 20, 34, 38, 39, 43, 37, 32, 7, 28, 23, 3, 14, 46, 36, 35, 12, 15, 20, 34, 38, 39, 43, 37, 32, 7, 28, 23, 49, 6]49, 6]
牌手
牌手1:1:方块方块4 4 方块方块8 8 方块方块A A 方块方块Q Q 红桃红桃3 3 红桃红桃5 5 红桃红桃J J 草花草花6 6 草花草花A A 黑桃黑桃10 10 黑桃黑桃4 4 黑桃黑桃5 5 黑桃黑桃K K
牌手
牌手2:2:方块方块6 6 方块方块J J 方块方块K K 红桃红桃10 10 红桃红桃2 2 红桃红桃9 9 红桃红桃A A 红桃红桃Q Q 草草花花4 4 黑桃黑桃2 2 黑黑桃桃3 3 黑桃黑桃6 6 黑桃黑桃7 7
牌手
牌手3:3:方块方块10 10 方块方块2 2 方块方块5 5 方块方块7 7 红桃红桃6 6 红桃红桃7 7 红桃红桃K K 草花草花2 2 草草花花J J 草花草花K K 草花草花Q Q 黑桃黑桃J J 黑桃黑桃Q Q
牌手
牌手4:4:方块方块3 3 方块方块9 9 红桃红桃4 4 红桃红桃8 8 草花草花10 10 草花草花3 3 草花草花5 5 草花草花7 7 草草花花8 8 草花草花9 9 黑桃黑桃8 8 黑桃黑桃9 9 黑桃黑桃AA"""
import random


def gen_pocker(n):
    random.shuffle(n)
    return n


# 产生牌的花色
def getColor(n):
    if 0 <= n <= 12:
        return "梅花"
    elif 13 <= n <= 25:
        return "方块"
    elif 26 <= n <= 38:
        return "红桃"
    elif 39 <= n <= 51:
        return "黑桃"


def getValue(n):
    if n == 0 or n == 13 or n == 26 or n == 39:
        return 'A'
    elif n == 12 or n == 38 or n == 25 or n == 51:
        return 'K'
    elif n == 11 or n == 37 or n == 24 or n == 50:
        return 'Q'
    elif n == 10 or n == 36 or n == 23 or n == 49:
        return 'J'
    else:
        return n % 13


def getPuk():
    list_poker = []  # 代表一副牌，现在表示还没有牌，只是一个牌盒
    for i in range(0, 52):
        list_poker.append(i)  # 按顺序往牌盒中放入52张牌
    list_poker = gen_pocker(list_poker)  # 将牌盒中的牌打乱顺序
    list1 = []  # 定义4个牌手
    list2 = []
    list3 = []
    list4 = []
    for i in range(0, 52):  # 实现发牌
        if i < 13:  # 打乱后的前13张牌发给牌手1，实现牌手1手牌中如何含有花色和数字
            list1.append(getColor(list_poker[i]) + str(getValue(list_poker[i])))
        elif i < 26:
            list2.append(getColor(list_poker[i]) + str(getValue(list_poker[i])))
        elif i < 39:
            list3.append(getColor(list_poker[i]) + str(getValue(list_poker[i])))
        else:
            list4.append(getColor(list_poker[i]) + str(getValue(list_poker[i])))
    print(list_poker)
    print("牌手1", list1)
    print("牌手2", list2)
    print("牌手3", list3)
    print("牌手4", list4)


getPuk()
