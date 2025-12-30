import math

print("--- Задание 1: Сравнение гипотенуз ---")

def calculate_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

print("Треугольник №1:")
leg1_a = float(input("  Введите первый катет: "))
leg1_b = float(input("  Введите второй катет: "))
hyp1 = calculate_hypotenuse(leg1_a, leg1_b)
print(f"  Гипотенуза №1 = {round(hyp1, 2)}")

print("Треугольник №2:")
leg2_a = float(input("  Введите первый катет: "))
leg2_b = float(input("  Введите второй катет: "))
hyp2 = calculate_hypotenuse(leg2_a, leg2_b)
print(f"  Гипотенуза №2 = {round(hyp2, 2)}")

print("\nРЕЗУЛЬТАТ СРАВНЕНИЯ:")
if hyp1 > hyp2:
    print("Гипотенуза первого треугольника БОЛЬШЕ.")
elif hyp1 < hyp2:
    print("Гипотенуза второго треугольника БОЛЬШЕ.")
else:
    print("Гипотенузы РАВНЫ.")


print("-" * 30)