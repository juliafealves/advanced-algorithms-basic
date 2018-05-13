# # -*- coding: utf-8 -*-
red, green, blue = map(int, raw_input().split())
bouquets = 0

if red == blue == green: bouquets = red
else:
    mix = 1
    while mix <= 3:
        if red >= mix and green >= mix and blue >= mix:
            r = (red - mix)/3
            g = (green - mix)/3
            b = (blue - mix)/3
            bouquets = max(bouquets, r + g + b + mix)

        mix += 1

    bouquets = max(bouquets, red / 3 + green / 3 + blue / 3)

print bouquets

