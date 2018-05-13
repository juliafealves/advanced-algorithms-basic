# -*- coding: utf-8 -*-
r, g, b = map(int, raw_input().split())
bouquets = 0

while r >= 3:
    bouquets += r / 3
    r %= 3

while g >= 3:
    bouquets += g / 3
    g %= 3

while b >= 3:
    bouquets += b / 3
    b %= 3

bouquets += min(r, g, b)
print bouquets