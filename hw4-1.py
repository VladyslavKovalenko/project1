list1 = list(map(int, input("Введите числа через пробел: ").split()))
list2 = []

count = 0

for i in list1:
    if i == 0:
        count += 1
    else:
        list2.append(i)

list2.extend([0] * count)

print("Список с нулями в конце:", list2)