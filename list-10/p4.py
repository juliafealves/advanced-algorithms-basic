# coding: utf-8
n, m = map(int, raw_input().split())
l = [0] * 100005
v = [False] * 100005
a = [0] * (100005 - n)
b = map(int, raw_input().split())
a = [0] + b + a

for i in xrange(n, 0, -1):
    if not v[a[i]]: l[i] += 1
    v[a[i]] = True
    l[i] += l[i + 1]

for _ in xrange(m):
    t = int(raw_input())
    print l[t]