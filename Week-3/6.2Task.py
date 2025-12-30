import math
print("--- Часть 2: Площадь выпуклого четырехугольника ---")

def triangle_area_heron(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

print("Введите длины сторон и диагональ:")
side1 = float(input("  Сторона 1: "))
side2 = float(input("  Сторона 2: "))

side3 = float(input("  Сторона 3: "))
side4 = float(input("  Сторона 4: "))

diag = float(input("  Диагональ: "))

area_triangle_1 = triangle_area_heron(side1, side2, diag)
area_triangle_2 = triangle_area_heron(side3, side4, diag)

total_area = area_triangle_1 + area_triangle_2

print(f"Площадь первого треугольника: {round(area_triangle_1, 2)}")
print(f"Площадь второго треугольника: {round(area_triangle_2, 2)}")
print(f"ОБЩАЯ ПЛОЩАДЬ ЧЕТЫРЕХУГОЛЬНИКА: {round(total_area, 2)}")