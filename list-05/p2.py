# -*- coding: utf-8 -*-
a = raw_input()
b = raw_input()
size = len(a)

i = 0
j = size

binary_b = ''
distance = 0
while j <= len(b):
    binary_b += b[i:j]

    i += 1
    j += 1

print binary_b
print distance