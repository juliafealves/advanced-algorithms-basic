# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: C. Stripe


def cumulative_sum(array):
    cumulative_sum = [0]

    for i in xrange(1, len(array) + 1):
        cumulative_sum.append(cumulative_sum[i - 1] + array[i - 1])

    return cumulative_sum


size = int(raw_input())
numbers = map(int, raw_input().split())

cumulative_sum = cumulative_sum(numbers)

slices = 0
last = len(cumulative_sum) - 1

for i in xrange(len(numbers) - 1):
    if (cumulative_sum[i + 1]) == (-cumulative_sum[i + 1] + cumulative_sum[last]):
        slices += 1

print slices