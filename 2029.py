n = int(input().strip())
current_position = 1
ans = 0

towers = [0] * (n + 1)
tower_chars = input().strip()
for i in range(1, n + 1):
    towers[i] = ord(tower_chars[i - 1]) - ord('@')

for ni in range(n, 0, -1):
    if current_position != towers[ni]:
        ans += 1 << (ni - 1)
        current_position = current_position ^ towers[ni]

print(ans)


