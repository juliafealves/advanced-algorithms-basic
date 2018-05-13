# -*- coding: utf-8 -*-
from math import sqrt

def sieve_prime(number):
    primes_sqrt = int(sqrt(number))
    primes = [True] * (number + 1)
    primes[0], primes[1] = False, False

    for i in xrange(2, primes_sqrt + 1):
        if primes[i]:
            for j in xrange(i * i, number + 1, i): primes[j] = False

    return primes

primes = sieve_prime(int(sqrt(10 ** 12)))
query = int(raw_input())
numbers = map(int, raw_input().split())

for number in numbers:
    square_root = sqrt(number)
    if square_root % int(square_root) != 0: print "NO"
    elif primes[int(square_root)]: print "YES"
    else: print "NO"
