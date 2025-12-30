num1 = float(input())
sign = input()
num2 = float(input())

if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/" and num2 != 0:
    print(num1 / num2)
elif sign == "/" and num2 == 0:
    print("Division by zero!")
else:
    print("Error")
