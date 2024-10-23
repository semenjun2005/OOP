from itertools import combinations
from math import factorial as fact
from math import ceil


def prime(n): #функция поиска всех простых чисел от 2 до n(алгоритм решета Эротосфена)
    primes = []
    ar = [True] * (n + 1)
    for i in range(2, n + 1):
        if ar[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                ar[j] = False
    return primes


def comb_without_rep(n, m):
    if m > n:
        return 0
    return fact(n) // (fact(m) * fact(n - m))


k, s = map(int, input().split())
result = 0

data_comb = map(lambda x: x[0] * x[1], combinations(prime(s), 2))


for i in data_comb: #цикл, который нужен для исключения лишних комбинаций, возникший на основе произведения простых чисел
    result -= comb_without_rep(ceil((s + 1 - i) / i), k) #(s + 1 - i) / j - количество групп, которое мы можем распределить по i элементов

for j in prime(s):
    result += comb_without_rep(ceil((s + 1 - j) / j), k) #количество комбинация из числа из k элементов из (s + 1 - j) / j) групп на основе числа j
    if result >= 10000:
        result = 10000
        break

print(result)