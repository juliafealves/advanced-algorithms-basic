# coding: utf-8

n = int(raw_input())
k = int(raw_input())
points = []

for _ in xrange(n):
    p = int(raw_input())
    points.append(p)

points.sort(reverse=True)

e = points[0]
w = 0

for p in xrange(len(points)):
    if e == points[p]: w += 1
    elif w >= k: break
    else: w += 1

    e = points[p]

print w
