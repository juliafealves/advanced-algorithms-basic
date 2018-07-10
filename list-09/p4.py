# coding: utf-8
n = int(raw_input())
A = map(int, raw_input().split())

s = 1
max_s = s

for i in xrange(1, len(A)):
    if A[i - 1] <= A[i]: s += 1
    else:
        if max_s <= s: max_s = s
        s = 1

if max_s <= s: max_s = s

print max_s