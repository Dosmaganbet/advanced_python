print("--- Часть 1: Вычитание дробей (A/B) - (C/D) ---")

def gcd_euclid(x, y):
    while y != 0:
        x, y = y, x % y
    return x

print("Введите первую дробь A/B:")
a = int(input("  A (числитель): "))
b = int(input("  B (знаменатель): "))

print("Введите вторую дробь C/D:")
c = int(input("  C (числитель): "))
d = int(input("  D (знаменатель): "))

numerator = (a * d) - (c * b)
denominator = b * d

common_divisor = gcd_euclid(abs(numerator), denominator)

final_num = numerator // common_divisor
final_den = denominator // common_divisor

print(f"Результат вычитания: {final_num}/{final_den}")
print("-" * 30)