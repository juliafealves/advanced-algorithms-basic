# coding: utf-8
n = int(raw_input())
a = map(int, raw_input().split())
unique = []
a.sort()
c = 0

for ai in a:
    e = ai
    while(True):
        if not e in unique:
            unique.append(e)
            break
        e += 1
        c += 1
print c
