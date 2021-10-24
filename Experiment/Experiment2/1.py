a = [1, 2, 3, 3, 4, 3, 1]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)
