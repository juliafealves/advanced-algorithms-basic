# coding: utf-8
def pow_mod(x, y, z):
    number = 1
    while y:
        if y & 1: number = number * x % z
        y >>= 1
        x = x * x % z

    return number

r = int(raw_input())
print pow_mod(3, r, 2 ** 31 - 1)