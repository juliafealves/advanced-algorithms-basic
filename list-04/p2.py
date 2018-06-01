# coding: utf-8
from math import sqrt

def sieve_prime(number):
    primes_sqrt = int(sqrt(number))
    primes = [True] * (number)
    primes[0], primes[1] = False, False

    for i in xrange(2, primes_sqrt + 1):
        if primes[i]:
            for j in xrange(i * i, number, i): primes[j] = False

    return primes

def twin_prime():
    twin_primes[3] = 1

    for p in xrange(5, MAX, 2):
        if primes[p] and primes[p + 2]:
            twin_primes[p] = 1
            twin_primes[p + 2] = 1

def cumulative_sum():
    sum = [twin_primes[0]]
    for i in xrange(1, len(twin_primes)): sum.append(sum[i - 1] + twin_primes[i])

    return sum

MAX = pow(10, 6) + 1
twin_primes = [0] * MAX
primes = sieve_prime(MAX)
twin_prime()

cumulative_sum = cumulative_sum()
q = int(raw_input())

for i in xrange(q):
    x, y = map(int, raw_input().split())
    print cumulative_sum[max(x, y)] - cumulative_sum[min(x, y) - 1]