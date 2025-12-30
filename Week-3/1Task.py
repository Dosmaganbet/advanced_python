import math

print("Выберите фигуру для расчета площади:")
print("1 - Прямоугольник")
print("2 - Треугольник")
print("3 - Круг")

choice = input("Введите номер фигуры (1, 2 или 3): ")

if choice == '1':
    width = float(input("Введите ширину: "))
    length = float(input("Введите длину: "))
    area = width * length
    print(f"Площадь прямоугольника: {area}")

elif choice == '2':
    base = float(input("Введите длину основания: "))
    height = float(input("Введите высоту: "))
    area = 0.5 * base * height
    print(f"Площадь треугольника: {area}")

elif choice == '3':
    radius = float(input("Введите радиус: "))
    area = math.pi * (radius ** 2)
    print(f"Площадь круга: {round(area, 2)}")

else:
    print("Ошибка: Неверный выбор. Пожалуйста, введите 1, 2 или 3. ")