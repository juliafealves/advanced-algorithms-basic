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

MAX = 10 ** 6
primes = sieve_prime(MAX)
query = int(raw_input())

for q in xrange(query):
    twin_primes = 0
    initial, end = map(int, raw_input().split())

    for number in xrange(initial, end + 1):
        if primes[number] and ((number <= MAX and primes[number + 2]) or primes[abs(number - 2)]): twin_primes += 1

    print twin_primes