f = int(input())
tasks = 12 - f
time = 4 * 60
if tasks * 45 < time:
    print('YES')
else:
    print('NO')