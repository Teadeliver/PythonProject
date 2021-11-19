list1 = eval(input())
list2 = list1.copy()
list2.sort()
list2.reverse()
dict1 = {}
for i in range(len(list1)):
    dict1.append(i, list1[i])
print(dict1)
print(list1)
print(list2)
list3 = []
if len(list1) == 0:
    print("0")
elif len(list1) == 1 or len(list1) == 2:
    print("1")
else:
    for i in range(int(len(list1) / 2)):
        list3.append(list2[i])
print(list3)
