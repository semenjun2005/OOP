import random

n = int(input())
balls_count = 0

for i in range(n):
    for position in range(balls_count):
        for cur_v in range(1, balls_count):
            cur_u = cur_v + 1
            print(f"? {cur_v} {cur_u}")

    balls_count = i + 2

    v = random.randint(1, balls_count - 1)
    u = v + 1
    print(f"! {v} {u}")
