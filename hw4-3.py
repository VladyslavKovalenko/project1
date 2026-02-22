import random

lengthList1 = random.randint(3, 10)
list1 = [random.randint(0, 100) for i in range(lengthList1)]

list2 = []

list2.append(list1[0])
list2.append(list1[2])
list2.append(list1[-2])
print(list1)
print(list2)