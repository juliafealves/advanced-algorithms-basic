# coding: utf-8
n = int(raw_input())
k = [0] * 100
c, t = 0, 1

while(True):
    if n <= 0: break
    b = n % 10
    c = max(b, c)

    for i in xrange(b): k[i] += t
    n /= 10
    t *= 10

print c
print ' '.join(map(str, k[:c]))
