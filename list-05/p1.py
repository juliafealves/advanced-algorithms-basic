# -*- coding: utf-8 -*-
def cumulative_sum(array):
    cumulative_sum = [0]

    for i in xrange(1, len(array) + 1): cumulative_sum.append(cumulative_sum[i - 1] + array[i - 1])

    return cumulative_sum

def binary_search(array, number):
    i, j = 0, len(array)

    while i <= j:
        m = (i + j) / 2
        middle = array[m]

        if middle == number: return m
        elif middle < number:
            after = m + 1

            if after < len(array) and array[after] >= number: return after
            i = after
        elif middle > number:
            before = m - 1

            if before >= 0 and array[before] == number: return before
            elif before >= 0 and array[before] < number: return m
            j = before

    return m

n = int(raw_input())
piles = map(int, raw_input().split())
m = int(raw_input())
worms = map(int, raw_input().split())

cumulative_sum = cumulative_sum(piles)

for worm in worms: print binary_search(cumulative_sum, worm)

