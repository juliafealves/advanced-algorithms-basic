# coding: utf-8
n, t = map(int, raw_input().split())
a = map(int, raw_input().split())
b = 0

while(True):
    if (t - 1 <= b): break
    b += a[b]

if (b == t - 1): print 'YES'
else: print 'NO'