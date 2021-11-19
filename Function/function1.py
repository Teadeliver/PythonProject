list1 = eval(input())
list2 = [list1[0], max(list1[0], list1[1])]
list3 = []
if len(list1) == 0:
    print("0")
else:
    list3.append(1)
    list3.append(1)
    for i in range(2, len(list1)):
        if list1[i] + list2[i - 2] >= list2[i - 1]:
            list2.append(list1[i] + list2[i - 2])
            list3.append(list3[i - 2] + 1)
        else:
            list2.append(list2[i - 1])
            list3.append(list3[i - 1])
print(list3[len(list1) - 1])
