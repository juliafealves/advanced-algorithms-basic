# coding: utf-8
n = int(raw_input())

if n % 2 != 0: print 0
else:
    if n % 4 == 0: print (n / 4) - 1
    else: print n / 4