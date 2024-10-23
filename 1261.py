from itertools import takewhile

n = int(input())

third_pow = list(takewhile(lambda x: x <= (2 ** 32 - 1) // 3,
                           (3 ** i for i in range(32))))

temp = 0
while n >= (third_pow[temp + 1] - 1) // 2:
    temp += 1

for count in range(1 << (temp + 1)): #битовый сдвиг
    ans = sum(third_pow[i] for i in range(temp + 1) if count & (1 << i))
    if ans <= n:
        continue
    tips = ans - n
    for k in range(temp, -1, -1):
        if tips >= third_pow[k]:
            tips -= third_pow[k]
    if tips == 0:
        print(ans, ans - n)
        break
else:
    print(0)