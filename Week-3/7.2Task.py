import math

print("--- Часть 2: Конвертация в 10-значный Octal код ---")

number = int(input("Введите целое неотрицательное число: "))

octal_code = f"{number:010o}"

print(f"Результат: {octal_code}")