# -*- coding: utf-8 -*-
from math import sqrt

def get_divisors(number):
    divisors = []

    for n in xrange(1, int(sqrt(number)) + 1):
        if number % n == 0:
            if number / n == n: divisors.append(n)
            else:
                divisors.append(n)
                divisors.append(number / n)
    divisors.sort(reverse=True)

    return divisors

def is_perfect_square(number):
    square = int(sqrt(number))
    return number == square * square

def exist_perfect_divisors(number):
    if number == 1: return False
    if is_perfect_square(number): return True
    for n in xrange(2, int(sqrt(number)) + 1):
        if number % n == 0:
            if is_perfect_square(n): return True
            if number / n != n and is_perfect_square(number / n): return True

    return False

n = int(raw_input())
divisors = get_divisors(n)

for d in divisors:
    if not exist_perfect_divisors(d):
        print d
        break
