n = int(input().strip())

v_min = []
v_max = []

if n % 2 == 1:
    up = 2
    down = n
    for i in range(n - 1):
        if i % 2 == 1:
            v_min.append(up)
            up += 2
        else:
            v_min.append(down)
            down -= 2
    v_min.append(1)
else:
    down = n
    up = 2
    i = 0
    while up <= down:
        if i % 2 == 1:
            v_min.append(up)
            up += 2
        else:
            v_min.append(down)
            down -= 2
        i += 1
    if n % 4 == 0:
        up = n // 2 + 1
        down = n // 2 - 1
        while len(v_min) < n:
            if up <= n:
                v_min.append(up)
                up += 2
            if down > 0:
                v_min.append(down)
                down -= 2
    else:
        v_min.append(n // 2)
        up = n // 2 + 2
        down = n // 2 - 2
        while len(v_min) < n:
            if up <= n:
                v_min.append(up)
                up += 2
            if down > 0:
                v_min.append(down)
                down -= 2

for i in range(1, n + 1, 2):
    v_max.append(i)
for i in range(n if n % 2 == 0 else n - 1, 0, -2):
    v_max.append(i)

start_index_min = v_min.index(1)
start_index_max = v_max.index(1)

for i in range(len(v_min)):
    print(v_min[(start_index_min + i) % len(v_min)], end=" ")
print()

for i in range(len(v_max)):
    print(v_max[(start_index_max + i) % len(v_max)], end=" ")
print()
