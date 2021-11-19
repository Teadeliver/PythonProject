a = input()
res = a
ans = 0
level = 0
a = a.replace('[', '')
a = a.replace(']', '')
nums = a.split(',')
b = res
for i in range(len(b)):
    if b[i] == '[':
        level += 1
    elif b[i] == ']':
        level -= 1
    elif b[i] == ',':
        continue
    elif b[i + 1] == ',' or b[i + 1] == ']':
        ans += 11 - level
print(ans)
