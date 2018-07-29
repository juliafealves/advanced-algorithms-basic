# coding: utf-8
n = int(raw_input())
v = map(int, raw_input().split())
u = sorted(v)
v1 = [0] * (n + 1)
u1 = [0] * (n + 1)
a = []

for i in xrange(1, n + 1):
    v1[i] = v1[i-1] + v[i-1]
    u1[i] = u1[i-1] + u[i-1]

m = int(raw_input())

for _ in xrange(m):
    t, l, r = map(int, raw_input().split())
    d = v1 if t == 1 else u1
    a.append(str(d[r] - d[l-1]))

print '\n'.join(a)