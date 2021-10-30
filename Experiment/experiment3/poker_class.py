# Card类：一张牌
class Card:
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['梅花', '方片', '红桃', '黑桃']

    # _init__()方法是一种特殊的方法，就是Java里的构造函数
    def __init__(self, rank, suit, face_up=True):  # self代表类的实例，而非类，类似于Java的This
        self.rank = rank  # 牌面数字1~13
        self.suit = suit  # 花色
        self.is_face_up = face_up  # 是否显示牌的正面，True为正面，False为反面

    def __str__(self):  # 重写print()方法，打印一张牌的信息
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def pic_order(self):  # 牌的顺序号
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

    def flip(self):  # 翻牌方法
        self.is_face_up = not self.is_face_up


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

    def give(self, card, other_hand):  # 把一张牌给其他选手
        self.cards.remove(card)
        other_hand.add(card)
        # other_hand.append(card)   	# 上面两行可以用这一行代替


# Poke类：一副牌
# 继承Hand类
class Poke(Hand):
    """Poke类代表一副牌，可以看做是有52张牌的牌手，所以继承Hand类。由于其中cards列表变量要存储52张牌
    而且要发牌，洗牌，所以增加方法如下方法:"""

    def populate(self):  # 生成一副牌
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):  # 洗牌
        import random
        random.shuffle(self.cards)  # 打乱牌的顺序

    def deal(self, hands, per_hand=13):  # 将牌发给玩家，每人默认13张牌
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                    # self.give(top_card,hand)	#上两句可以用此句替换
                else:
                    print('不能继续发牌了，牌已经发完了!')


"""
if __name__ == '__main__':的作用
一个python文件通常有两种使用方法，
第一是作为脚本直接执行，
第二是 import 到其他的 python 脚本中被调用（模块重用）执行。
因此 if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
在 if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
而 import 到其他脚本中是不会被执行的。
"""
if __name__ == "__main__":
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
