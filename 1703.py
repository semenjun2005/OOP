import math
from math import sqrt, acos, pi, sin, cos

def scalar_prod(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def vec_prod(a, b):
    return [a[1] * b[2] - a[2] * b[1], - (a[0] * b[2] - a[2] * b[0]),
            a[0] * b[1] - a[1] * b[0]]

def length(a):
    return sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)

a, b = map(float, input().split())
v0 = list(map(float, input().split()))
v1 = list(map(float, input().split()))
zeros = [0, 0, 0]

v0_arm = [zeros[i] - v0[i] for i in range(3)]
v1_arm = [v1[i] - v0[i] for i in range(3)]
dot = [v0[i] + v1_arm[i] * scalar_prod(v0_arm, v1_arm) / (scalar_prod(v1_arm, v1_arm)) for i in range(3)]
rad = [dot[i] - zeros[i] for i in range(3)]

d = length([zeros[i] - dot[i] for i in range(3)])

ang1 = acos(max(-1, min((b ** 2 - a ** 2 - d ** 2) / (-2 * a * d), 1)))
ang2 = acos(max(-1, min((d ** 2 - a ** 2 - b ** 2) / (-2 * a * b), 1)))

if d > a + b or ang2 < pi / 2 - 1e-9:
    print("No solution.")
else:
    unit_vec = vec_prod(v1_arm, rad)
    unit_vec = [i / length(unit_vec) for i in unit_vec]
    res = [rad[i] / length(rad) * a * cos(ang1) +
           unit_vec[i] * a * sin(ang1) for i in range(3)]

    print(f"{res[0]:.20f} {res[1]:.20f} {res[2]:.20f} {ang2:.20f}")