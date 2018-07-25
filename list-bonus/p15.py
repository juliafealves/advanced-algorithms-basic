# coding: utf-8
n = int(raw_input())
ticket = raw_input()
digits = map(int, list(ticket))
only_numbers = set(7, 4)

p1 = digits[:n/2]
p2 = digits[:n/2]

if only_numbers.difference(set(p1)) == only_numbers: print 'YES'
else: print 'NO'
print digits