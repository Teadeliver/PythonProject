s = [9, 7, 8, 3, 2, 1, 5, 6]
for i in range(len(s)):
    if (s[i] % 2 == 0):
        s[i] = s[i] ** 2
    else:
        continue
print(s)
