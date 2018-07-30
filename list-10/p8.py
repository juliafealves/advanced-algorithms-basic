# coding: utf-8
from math import sqrt, ceil
r, x, y, x2, y2 = map(int, raw_input().split())
p = sqrt(pow(x2 - x, 2) + pow(y2 - y, 2))
print int(ceil(p / r / 2.0))