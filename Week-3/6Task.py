import math

print("--- Часть 1: НОД (GCD) и НОК (LCM) ---")

def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

gcd_val = gcd_euclid(num1, num2)

lcm_val = (num1 * num2) // gcd_val

print(f"НОД (GCD) чисел {num1} и {num2} = {gcd_val}")
print(f"НОК (LCM) чисел {num1} и {num2} = {lcm_val}")
print("-" * 30)