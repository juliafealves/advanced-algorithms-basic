# -*- coding: utf-8 -*-
def cumulative_sum(array):
    sum = [array[0]]

    for i in xrange(1, len(array)): sum.append(sum[i - 1] + array[i])

    return sum

def binary_search(array, number):
    i, j = 0, len(array)
    position = -1

    while i <= j:
        m = (i + j) / 2
        middle = array[m]

        if middle < number: i = m + 1
        elif middle >= number:
            position = m
            j = m - 1

    return position + 1

n = int(raw_input())
piles = map(int, raw_input().split())
m = int(raw_input())
worms = map(int, raw_input().split())

sum = cumulative_sum(piles)

for worm in worms:
    if worm <= sum[0]: print 1
    elif sum[-2] < worm <= sum[-1]: print len(sum)
    else: print binary_search(sum, worm)

