from math import factorial as fact


def comb_without_rep(n, m):
    if m > n:
        return 0
    return fact(n) // (fact(m) * fact(n - m))


def counter(border, k, b):
    if border < b:
        if (k <= 1 and border > 0) or (border == 0 and k == 0):
            return True
        else:
            return False
    cur_pow = 1 #высшая степень
    var_pows = 0 #степень
    while cur_pow * b <= border:
        cur_pow *= b
        var_pows += 1
    if border // cur_pow >= 2:
        combinations1 = comb_without_rep(var_pows, k - 1)
        if k != 0:
            combinations2 = comb_without_rep(var_pows, k)
        else:
            combinations2 = 0
        return combinations1 + combinations2

    elif border // cur_pow == 1:
        combinations1 = comb_without_rep(var_pows, k)
        if k != 0:
            combinations2 = counter(border - cur_pow, k - 1, b)
        else:
            combinations2 = 0
        return combinations1 + combinations2


x, y = map(int, input().split())
k = int(input())
b = int(input())

print(counter(y, k, b) - counter(x - 1, k, b))