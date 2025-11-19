list1 = [4,1,3,4,4]
list2 = []
for i in list1:
    # if list2.count(i)==0:
    if not i in list2:
        list2.append(i)
print(list2)

