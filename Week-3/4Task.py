print("--- Часть 1: Деление дробей (A/B) / (C/D) ---")

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

new_numerator = a * d
new_denominator = b * c
common_divisor = gcd_euclid(new_numerator, new_denominator)
final_num = new_numerator // common_divisor
final_den = new_denominator // common_divisor

print(f"Результат деления: {final_num}/{final_den}")
print("-" * 30)