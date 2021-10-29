"""
编写程序，定义一个求 Fibonacci （斐波那契）数列的函数 fib( n)n)，并
编写测试代码，输出前 20 项（每项宽度 5 个字符位置，右对齐），每行
输出 10 个。请分别使用递归和 非递归方式 实现。 运行效果如下所示。
1         1         2         3         5         8        13        21        34        55
89       144       233       377       610       987      1597      2584      4181      6765
"""


def fib_recursion(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_norecursion(n):
    num1 = 1
    num2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 2):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return num2


print("递归方式：")
for i in range(20):
    print(format(fib_recursion(i + 1), '>10.0f'), end='')
    if (i + 1) % 10 == 0:
        print()
print("非递归方式")
for i in range(20):
    print(format(fib_norecursion(i + 1), '>10.0f'), end='')
    if (i + 1) % 10 == 0:
        print()
