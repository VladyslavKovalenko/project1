list1 = list(map(int, input("Введите числа через пробел: ").split()))


if not list1:
    res = 0
else:
    sumChet = sum(list1[::2])
    res = sumChet * list1[-1]

print(res)