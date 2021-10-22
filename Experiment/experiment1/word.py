import random

from random_words import RandomWords

print("欢迎参加猜单词游戏")
print("把字母组合成一个正确的单词.")
key_in = 'Y'
while 1:
    if key_in == 'Y' or key_in == 'y':
        word = RandomWords().random_word()
        word_true = word
        word_change = ''
        while word:
            position = random.randrange(len(word))
            word_change += word[position]
            word = word[:position] + word[position + 1:]
        print(word_true)
        print("乱序后单词:{0}".format(word_change))
        guess = str(input("请你猜: "))
        while 1:
            if guess == word_true:
                print("真棒，你猜对了!")
                break
            else:
                print("对不起不正确.")
                guess = str(input("继续猜: "))
    key_in = input("是否继续（Y/N)：")
    if key_in == 'N' or key_in == 'n':
        break
