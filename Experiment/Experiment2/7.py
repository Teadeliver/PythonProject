a = int(input("输入被除数："))
b = int(input("输入除数："))
assert b != 0, "除数不能为0"
x = a / b
print(a, '/', b, '=', x)
