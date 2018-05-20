# -*- coding: utf-8 -*-
def exist_divisible(number, max=10):
    for i in xrange(1, max):
        if i % number == 0: return i

    return -1


digits, divisible = map(int, raw_input().split())

if digits == 1: print exist_divisible(divisible)
else:
    repeat = digits - 1 if divisible != 10 else digits - 2
    print str(divisible) + '0' * repeat