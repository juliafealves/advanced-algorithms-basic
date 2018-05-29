# https://www.urionlinejudge.com.br/judge/pt/problems/view/1926
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

def twin_prime():
    twin_primes.append(3)

    for p in xrange(5, MAX + 1, 2):
        if primes[p] and primes[p + 2]:
            twin_primes.append(p)
            twin_primes.append(p + 2)

def cumulative_sum():
    sum = [twin_primes[0]]

    for i in xrange(1, len(twin_primes)): sum.append(sum[i - 1] + twin_primes[i])

    return sum

MAX = pow(10, 6) + 1
twin_primes = []
primes = sieve_prime(MAX)
twin_prime()

cumulative_sum = cumulative_sum()
print twin_primes
print cumulative_sum
q = int(raw_input())

for i in xrange(q):
    x, y = map(int, raw_input().split())
    print len(twin_primes[:max(x , y) + 1])