# coding: utf-8
MAX = 100005
memo = [0] * MAX
a = [0] * MAX

n = int(raw_input())
b = map(int, raw_input().split())

for i in b: a[i] = a[i] + 1

memo[1] = a[1]

for i in xrange(2, 100001):
    memo[i] = max(memo[i - 1], memo[i - 2] + i * a[i])

print memo[100000]