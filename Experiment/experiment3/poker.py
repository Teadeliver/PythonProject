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
