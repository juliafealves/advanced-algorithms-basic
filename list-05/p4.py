# -*- coding: utf-8 -*-
n = int(raw_input())
posibilities = 0

for i in xrange(1, n + 1): posibilities += pow(2, i)

print posibilities