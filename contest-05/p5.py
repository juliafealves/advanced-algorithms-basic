# coding: utf-8
from collections import Counter

exist = Counter()
n = int(raw_input())
a = map(int, raw_input().split())
a.sort()
m = max(a)

i, j = 1, 0

while j < len(a):
    e = a[j]

    if exist[e]:
        j += 1
        continue
    elif e == i:
        exist[e] = 1
        i += 1
        j += 1
    elif e < i:
        j += 1
        continue
    else:
        s = e - (e - i)
        exist[s] = 1
        i += 1
        j += 1

print max(exist.keys()) + 1