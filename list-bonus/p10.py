# coding: utf-8
k = int(raw_input())
s = raw_input()
p = [0] * (len(s) + 1)
p[0] = 1
m, c = 0, 0

for i in xrange(len(s)):
    if s[i] == '1': m += 1
    if m >= k: c += p[m-k]
    p[m] += 1

    i += 1
print c