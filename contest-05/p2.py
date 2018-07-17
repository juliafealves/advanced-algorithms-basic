# coding: utf-8
n = int(raw_input())
x = map(int, raw_input().split())
y = map(int, raw_input().split())
x.pop(0)
y.pop(0)

u = set(x).union(set(y))

if len(u) == n: print 'I become the guy.'
else: print 'Oh, my keyboard!'