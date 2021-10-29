"""
编写程序，利用元组作为函数的返回值，求系列类型中的最大值、最小值和元素个数，并编写测试代码，
假设测试数据分别为s1=[9,8,7,3,2,1,55,6]、s2=['apple','pear','melon','kiwi'],s3='TheQuickBrownFox'。
运行效果如下：s1=[9,8,7,3,2,1,55,6]
最大值=55，最小值=1，元素个数=8
s2=['apple','pear','melon','kiwi']
最大值=pear，最小值=apple，元素个数=4
s3='TheQuickBrownFox'
最大值=x，最小值=B，元素个数=16
提示：函数形参为系列类型，返回值是形如“（最大值，最小值，元素个数）”的元组
"""


def print_info(x):
    max_num = max(x)
    min_num = min(x)
    len_num = len(x)
    print("最大值是%s" % max_num)
    print("最小值是%s" % min_num)
    print("元素个数是{0}".format(len_num))
    return max_num, min_num, len_num


s1 = [9, 8, 7, 3, 2, 1, 55, 6]
s2 = ['apple', 'pear', 'melon', 'kiwi']
s3 = 'TheQuickBrownFox'
q = print_info(s1)
print(q)
w = print_info(s2)
print(w)
e = print_info(s3)
print(e)
