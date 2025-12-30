print("--- Часть 2: Точки внутри круга ---")

def is_inside_circle(x, y, center_a, center_b, radius_sq):
    distance_sq = (x - center_a)**2 + (y - center_b)**2
    if distance_sq <= radius_sq:
        return True
    else:
        return False

print("Параметры круга:")
circle_a = float(input("  Введите координату центра a (x): "))
circle_b = float(input("  Введите координату центра b (y): "))
radius = float(input("  Введите радиус R: "))
r_squared = radius ** 2

points_inside = 0

print("Введите координаты точки P:")
p1 = float(input("  p1 (x): "))
p2 = float(input("  p2 (y): "))
if is_inside_circle(p1, p2, circle_a, circle_b, r_squared):
    points_inside += 1
    print("  -> Точка P внутри!")
else:
    print("  -> Точка P снаружи.")

print("Введите координаты точки F:")
f1 = float(input("  f1 (x): "))
f2 = float(input("  f2 (y): "))
if is_inside_circle(f1, f2, circle_a, circle_b, r_squared):
    points_inside += 1
    print("  -> Точка F внутри!")
else:
    print("  -> Точка F снаружи.")

print("Введите координаты точки L:")
l1 = float(input("  l1 (x): "))
l2 = float(input("  l2 (y): "))
if is_inside_circle(l1, l2, circle_a, circle_b, r_squared):
    points_inside += 1
    print("  -> Точка L внутри!")
else:
    print("  -> Точка L снаружи.")

print(f"\nВсего точек внутри круга: {points_inside}")