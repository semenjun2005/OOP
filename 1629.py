n = int(input().strip())
res = 0

for _ in range(n - 1):
    q, d, t = map(int, input().strip().split())
    flight_times = []
    dep_times = input().strip().split()
    for i in dep_times:
        dep_hours, dep_minutes = map(int, i.split(':'))
        midnight = 60 * dep_hours + dep_minutes
        flight_times.extend(
            midnight + k * 24 * 60 + d
            for k in range(2 * n + 1)
        )
    nxt = min(j for j in flight_times if j >= res)
    res = nxt + t

print(res)
