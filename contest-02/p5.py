# coding: utf-8
from collections import Counter

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

while True:
    n = int(raw_input())
    if n == 0: break

    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    pairs = Counter()

    for i in a:
        for j in b:
            if gcd(i, j) == 1:
                if not pairs[(i, j)]: pairs[(i, j)] = 1
                if not pairs[(j, i)]: pairs[(j, i)] = 1

    print len(pairs.items())