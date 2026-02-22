input_list = input("Введіть елементи списку через пробіл: ").split()
if len(input_list) > 1:
    input_list.insert(0, input_list[-1])
    del input_list[-1]

print(input_list)