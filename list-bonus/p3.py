# coding: utf-8
m, s = map(int, raw_input().split())
a = [9] * m
b = [0] * m
d = sum(a) - s

if d < 0 or (s == 0 and m > 1): print '-1 -1'
else:
    i = 0
    while(True):
        if d == 0: break
        if a[i] == 1 and i == 0 and len(a) > 1: i += 1
        if i >= len(a): break
        if a[i] == 0 and i > 0: i += 1
        if i >= len(a): break

        if d > 0:
            a[i] -= 1
            d -= 1

    i = 0
    while (True):
        if s == 0: break
        if b[i] == 9: i += 1
        if i >= len(b): break

        if s > 0:
            b[i] += 1
            s -= 1

    p1 = ''.join(map(str, a))
    p2 = ''.join(map(str, b))
    print '%s %s' % (p1, p2)