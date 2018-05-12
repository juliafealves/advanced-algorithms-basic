# -*- coding: utf-8 -*-
from math import sqrt

def is_prime(number):
    if number <= 1: return False
    if number == 2: return True
    if number % 2 == 0: return False

    for n in xrange(3, int(sqrt(number)) + 1, 2):
        if number % n == 0: return False

    return True

query = int(raw_input())

for q in xrange(query):
    number = int(raw_input())
    print 'Prime' if is_prime(number) else 'Not Prime'