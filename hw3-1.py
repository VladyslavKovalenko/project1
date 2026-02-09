num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))

diya = input("Действие над числами: ")

if(diya == "+"):
    print(num1 + num2)
elif(diya == "-"):
    print(num1 - num2)
elif(diya == "*"):
    print(num1 * num2)
elif(diya == "/") and (num2 != 0):
    print(num1 / num2 )