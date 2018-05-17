# -*- coding: utf-8 -*-
def cumulative_sum(array):
    cumulative_sum = [0]

    for i in xrange(1, len(array) + 1): cumulative_sum.append(cumulative_sum[i - 1] + array[i - 1])

    return cumulative_sum

def binary_search(array, number):
    i, j = 0, len(array)

    while i < j:
        m = (i + j) / 2
        middle = array[m]
        before = array[m - 1]

        if m - 1 >= 0:
            if before <= number <= middle:
                return m - 1 if before == number else m
            elif before > number < middle: j = m - 1
            else: i = m + 1

    return m

n = int(raw_input())
piles = map(int, raw_input().split())
m = int(raw_input())
worms = map(int, raw_input().split())

cumulative_sum = cumulative_sum(piles)

for worm in worms: print binary_search(cumulative_sum, worm)

