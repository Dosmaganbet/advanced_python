import math

print("--- Часть 1: Площадь четырехугольника ---")

def calculate_rectangle_area(a, b):
    return a * b

def calculate_right_triangle_area(leg1, leg2):
    rect_area = calculate_rectangle_area(leg1, leg2)
    return rect_area / 2

def heron_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Введите длины сторон (X и Y образуют прямой угол):")
x = float(input("  Сторона X: "))
y = float(input("  Сторона Y: "))
z = float(input("  Сторона Z: "))
t = float(input("  Сторона T: "))

area_part1 = calculate_right_triangle_area(x, y)

diagonal = math.sqrt(x**2 + y**2)

area_part2 = heron_area(z, t, diagonal)

total_area = area_part1 + area_part2

print(f"Площадь первой части (прямоугольной): {round(area_part1, 2)}")
print(f"Площадь второй части (по Герону): {round(area_part2, 2)}")
print(f"ОБЩАЯ ПЛОЩАДЬ: {round(total_area, 2)}")
print("-" * 30)