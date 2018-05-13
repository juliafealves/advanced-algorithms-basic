# -*- coding: utf-8 -*-
number = raw_input()
books = int(number)
digits = len(number)

numbers = 0
for n in xrange(1, digits):
    numbers += (int(str(9) * n) - int(str(1) + str(0) * (n - 1)) + 1) * n

numbers += (books - 10 ** (digits - 1) + 1) * digits

print numbers