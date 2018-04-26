# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Laser Sculpture - Ad-hoc

while True:
    dimension = map(int, raw_input().split())
    height = dimension[0]
    length = dimension[1]

    if height == length == 0:
        break

    final_height = map(int, raw_input().split())
    times = height - final_height[0]

    for i in xrange(1, len(final_height)):
        if final_height[i] < final_height[i - 1]:
            times += final_height[i - 1] - final_height[i]

    print times
