def mypow(a, b):
    return a ** b


def cifre(n):
    return len(str(n))


def Q(KK, M):
    """ Находит минимальное N для заданных K и M. """
    Mc = 0
    Kp = KK
    k = 0

    while Kp != 0:
        k += 1
        r = Kp % 10
        if Kp >= 10:
            Mc += r * (mypow(10, k) - 1) // 9 + 1
        else:
            Mc += (r - 1) * (mypow(10, k) - 1) // 9 + 1
        Kp //= 10

    if Mc > M:
        return 0
    elif Mc == M:
        return KK

    K = KK
    N = mypow(10, cifre(K))

    if K * 10 - N != 0:
        Mc += 1

    while Mc < M:
        if (M - Mc) < (K * 10 - N):
            N += M - Mc
            return N
        elif K * 10 - N != 0:
            Mc += K * 10 - N
            N *= 10
        else:
            return 0
        K *= 10

    if M == Mc:
        return N
    else:
        return 0



K, M = map(int, input().split())
print(Q(K, M))

