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
    List = []  # 代表一副牌，现在表示还没有牌，只是一个牌盒
    for i in range(0, 52):
        List.append(i)  # 按顺序往牌盒中放入52张牌
    List = gen_pocker(List)  # 将牌盒中的牌打乱顺序
    List1 = []  # 定义4个牌手
    List2 = []
    List3 = []
    List4 = []
    for i in range(0, 52):  # 实现发牌
        if i < 13:  # 打乱后的前13张牌发给牌手1，实现牌手1手牌中如何含有花色和数字
            List1.append(getColor(List[i]) + str(getValue(List[i])))
        elif i < 26:
            List2.append(getColor(List[i]) + str(getValue(List[i])))
        elif i < 39:
            List3.append(getColor(List[i]) + str(getValue(List[i])))
        else:
            List4.append(getColor(List[i]) + str(getValue(List[i])))
    print(List)
    print("牌手1", List1)
    print("牌手2", List2)
    print("牌手3", List3)
    print("牌手4", List4)


getPuk()
