# coding: utf-8
k = int(raw_input())
s = raw_input()
z = map(int, s)
l = []

i = 0
j = len(z)
m = 1

while True:
    if i == j:
        i = m
        m += 1

    if m >= j: break

    if sum(z[i:j]) == k:
        t = (i, j)

        if not t in l: l.append(t)

    i += 1

print l
print len(l)