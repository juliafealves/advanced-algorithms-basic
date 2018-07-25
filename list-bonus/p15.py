# coding: utf-8
n = int(raw_input())
ticket = raw_input()
digits = map(int, list(ticket))

p1 = digits[:n/2]
p2 = digits[n/2:]

if len(set(digits).difference(set([7,4]))) == 0 or len(set(digits).difference(set([7]))) == 0 or len(set(digits).difference(set([4]))) == 0:
    if sum(p1) == sum(p2): print 'YES'
    else: print 'NO'
else: print 'NO'
