s = int(input())
num_sum = 0
i = 0
while s != -1:
    num_sum += s
    i = i + 1
    s = int(input())
acer = float(num_sum / i)
print("sum = {0},aver = {1}".format(num_sum, acer))
