def is_level(lev, pos):

    s1 = [0, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    s2 = [0, 1, 3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1]

    if pos % 12 == 0:
        pos += 1
    return s1[pos % 12] if lev % 2 == 1 else s2[pos % 12]

def baga_mare(lev, pos, n, s):
    if lev == n:
        return pos
    fiu = 2 * pos - 1
    if s[n - lev] == is_level(lev + 1, fiu):
        return baga_mare(lev + 1, fiu, n, s)
    fiu = 2 * pos
    if s[n - lev] == is_level(lev + 1, fiu):
        return baga_mare(lev + 1, fiu, n, s)
    return 0

n = int(input())
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = int(input())

result = baga_mare(0, 1, n, s) - 1
print(result)

