# -*- coding: utf-8 -*-
def gcd(a, b):
    if (b == 0): return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


n, a, b, p, q = map(int, raw_input().split())

a_divisor = int(n / a)
b_divisor = int(n / b)
common_divisor = int(n/ lcm(a, b))

print a_divisor * p + b_divisor * q - common_divisor * min(p, q)