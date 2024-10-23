import math


# Считываем количество точек и радиус
n, r = map(float, input().split())
n = int(n)  # Приводим количество точек к целому числу

x1, y1 = map(float, input().split())
xPr, yPr = x1, y1
Summ = 0.0

for i in range(n - 1):
    x, y = map(float, input().split())
    a = x - xPr
    b = y - yPr
    xPr, yPr = x, y
    Summ += math.sqrt(a * a + b * b)
    if i == n - 2:
        a = x - x1
        b = y - y1
        Summ += math.sqrt(a * a + b * b)
Summ += 2 * math.pi * r

(f"{Summ:.2f}")

