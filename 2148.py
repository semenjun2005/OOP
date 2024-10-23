x_circle, y_circle, r = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x_mid = (x1 + x2) / 2
y_mid = (y1 + y2) / 2
x_height = x_mid - x_circle
y_height = y_mid - y_circle

if (x_height ** 2 + y_height ** 2) <= r ** 2:
    print('No way')
else:
    leng = (x_height ** 2 + y_height ** 2) ** 0.5
    x_height = x_height / leng * r
    y_height = y_height / leng * r
    x_dot = x_height + x_circle
    y_dot = y_height + y_circle
    print(x_dot, y_dot)