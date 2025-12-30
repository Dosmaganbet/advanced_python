print("--- Часть 2: Все делители числа ---")

number = int(input("Введите натуральное число: "))

print(f"Делители числа {number}:", end=" ")

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")

print()