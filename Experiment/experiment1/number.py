import random


def caculate(n1, n2):
    if n1 % n2 == 0:
        return n2
    return caculate(n2, n1 % n2)


num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
if num1 < num2:
    num1, num2 = num2, num1
print("整数 1={0}，整数 2={1}".format(num1, num2))
print("最大公约数是={0}，最小公倍数是={1}".format(caculate(num1, num2), int(num1 * num2 / caculate(num1, num2))))
