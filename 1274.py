from math import gcd

def parse_fraction(s):
    sign = -1 if s.startswith('-') else 1
    if sign == -1:
        s = s[1:]

    if ' ' in s:
        whole, frac = s.split()
        whole = int(whole)
    else:
        whole, frac = 0, s

    if '/' in frac:
        num, denom = map(int, frac.split('/'))
    else:
        num, denom = int(frac), 1

    num = sign * (whole * denom + num)
    return num, denom

def format_fraction(num, denom):
    sign = '-' if num < 0 else ''
    num = abs(num)
    whole = num // denom
    num = num % denom
    if whole == 0 and num == 0:
        return '0'
    elif num == 0:
        return f"{sign}{whole}"
    elif whole == 0:
        return f"{sign}{num}/{denom}"
    else:
        return f"{sign}{whole} {num}/{denom}"

def add_fractions(n1, d1, n2, d2):
    num = n1 * d2 + n2 * d1
    denom = d1 * d2
    return num, denom

def subtract_fractions(n1, d1, n2, d2):
    num = n1 * d2 - n2 * d1
    denom = d1 * d2
    return num, denom

def multiply_fractions(n1, d1, n2, d2):
    num = n1 * n2
    denom = d1 * d2
    return num, denom

def divide_fractions(n1, d1, n2, d2):
    num = n1 * d2
    denom = d1 * n2
    if denom < 0:  # to ensure denominator is positive
        num = -num
        denom = -denom
    return num, denom

def reduce_fraction(num, denom):
    common_divisor = gcd(abs(num), denom)
    return num // common_divisor, denom // common_divisor

# Чтение данных
frac1 = input().strip()
operation = input().strip()
frac2 = input().strip()

# Разбор дробей
n1, d1 = parse_fraction(frac1)
n2, d2 = parse_fraction(frac2)

# Вычисление результата
if operation == '+':
    result_num, result_denom = add_fractions(n1, d1, n2, d2)
elif operation == '-':
    result_num, result_denom = subtract_fractions(n1, d1, n2, d2)
elif operation == '*':
    result_num, result_denom = multiply_fractions(n1, d1, n2, d2)
elif operation == '/':
    result_num, result_denom = divide_fractions(n1, d1, n2, d2)

# Сокращение результата
result_num, result_denom = reduce_fraction(result_num, result_denom)

# Форматирование результата
result = format_fraction(result_num, result_denom)
print(result)
