num1 = float(input())
sign = input()
num2 = float(input())

if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2)
else:
    print("Ошибка: неверный знак")
