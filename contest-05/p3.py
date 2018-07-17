# coding: utf-8
n, c = map(int, raw_input().split())
x = map(int, raw_input().split())
results = [0]

for i in xrange(n - 1):
    if x[i] > x[i + 1]: results.append(x[i] - c - x[i + 1])

print max(results)