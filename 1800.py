data = input().split()
l = int(data[0]) / 100
h = int(data[1]) / 100
w = int(data[2]) / 60
if l / 2 < h:
    time = (2 * (h - l / 2) / 9.81) ** 0.5
    a = w * time
    if 0.25 < a % 1 < 0.75:
        print("bread")
    else:
        print("butter")
else:
    print("butter")