# Card类：一张牌
class Card:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['梅花', '方片', '红桃', '黑桃']

    # _init__()方法是一种特殊的方法，就是Java里的构造函数
    # __str__()方法是一种重写的方法，类似于Java里的重写toString方法
    def __init__(self, rank, suit):  # self代表类的实例，而非类，类似于Java的This
        self.rank = rank  # 牌面数字1~13
        self.suit = suit  # 花色

    def __str__(self):  # 重写print()方法，打印一张牌的信息
        return self.suit + self.rank

    def pic_order(self):  # 牌的顺序号,将牌面转换为数字顺序号
        if self.rank == 'A':
            face_num = 1
        elif self.rank == 'J':
            face_num = 11
        elif self.rank == 'Q':
            face_num = 12
        elif self.rank == 'K':
            face_num = 13
        else:
            face_num = int(self.rank)
        if self.suit == '梅花':
            suit = 1
        elif self.suit == '方片':
            suit = 2
        elif self.suit == '红桃':
            suit = 3
        else:
            suit = 4
        return (suit - 1) * 13 + face_num


# Hand类：一手牌
class Hand:

    def __init__(self):
        self.cards = []  # cards列表变量存储牌手手里的牌

    def __str__(self):  # 重写print()方法，打印出牌手的所有牌
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '无牌'
        return rep

    def clear(self):  # 清空手里的牌
        self.cards = []

    def add(self, card):  # 增加手里的牌
        self.cards.append(card)


# Poke类：一整副牌
# 继承Hand类
class Poke(Hand):
    # Poke类代表一副牌，可以看做一个有52张牌的特殊牌手，所以继承Hand类
    # 在Hand类中方法的基础上增加方法完成洗牌发牌等操作
    def populate(self):  # 生成一副牌,双循环按顺序生成，后续进行打乱
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):  # 洗牌
        import random
        random.shuffle(self.cards)  # 打乱牌的顺序

    def deal(self, hands, per_hand=13):  # 将牌发给玩家，每人默认13张牌
        for rounds in range(per_hand):
            for hand_x in hands:  # 四个牌手
                if self.cards:  # 判断是不是还有牌
                    top_card = self.cards[0]  # 类似于栈，读取顶上的一张牌
                    self.cards.remove(top_card)  # 移除顶上的一张牌
                    hand_x.add(top_card)  # 将顶上的牌给牌手
                else:
                    print('不能继续发牌了，牌已经发完了!')


# if __name__ == '__main__':的作用
# 一个python文件通常有两种使用方法，
# 第一是作为脚本直接执行，
# 第二是 import 到其他的 python 脚本中被调用（模块重用）执行。
# 因此 if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
# 在 if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
# 而 import 到其他脚本中是不会被执行的。
if __name__ == "__main__":  # 直接执行的话不用这句话也没事
    print('This is a module with classes for playing cards.')
    players = [Hand(), Hand(), Hand(), Hand()]
    poke = Poke()
    poke.populate()  # 生成一副牌
    poke.shuffle()  # 洗牌
    poke.deal(players, 13)  # 发给每人13张牌
    n = 1
    for hand in players:
        print('牌手', n, end=':')
        print(hand)
        n = n + 1
