lst = list(map(int, input().split()))

mid = len(lst) // 2
first = lst[:mid]
second = lst[mid:]
res = first + second

if (len(lst) % 2 != 0):
    mid = len(lst) // 2
    first = lst[:mid + 1]
    second = lst[mid + 1:]


print(res)
print(lst, "=>", first, second)



'''
[1, 2, 3] => [[1, 2], [3]]
[1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
[1] => [[1], []]
[] => [[], []] '''


