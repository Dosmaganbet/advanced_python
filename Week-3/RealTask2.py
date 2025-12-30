import math
def get_triangle_area(side):
    area = (math.sqrt(3) / 4) * (side ** 2)
    return area

print("--- Часть 1: Площадь гексагона (шестиугольника) ---")

a = float(input("Введите сторону шестиугольника (a): "))

one_triangle = get_triangle_area(a)

hexagon_area = 6 * one_triangle

print(f"Площадь шестиугольника: {round(hexagon_area, 2)}")
print("-" * 30)


print("--- Часть 2: Площадь трех прямоугольников ---")

for i in range(3):
    print(f"Прямоугольник номер {i + 1}:")
    
    side1 = float(input("  Введите первую сторону: "))
    side2 = float(input("  Введите вторую сторону: "))
    
    rect_area = side1 * side2
    
    print(f"  Площадь этого прямоугольника: {rect_area}")
    print(" ")