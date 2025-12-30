print("--- Часть 2: Площадь трех прямоугольников ---")

for i in range(3):
    print(f"Прямоугольник номер {i + 1}:")
    
    side1 = float(input("  Введите первую сторону: "))
    side2 = float(input("  Введите вторую сторону: "))
    
    rect_area = side1 * side2
    
    print(f"  Площадь этого прямоугольника: {rect_area}")
    print(" ")