# coding: utf-8
from math import acos, degrees, ceil
a, b, c = map(int, raw_input().split())

try:
    angle_a = ceil(degrees(acos((pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2.0 * a * b))))
    angle_b = ceil(degrees(acos((pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2.0 * b * c))))
    angle_c = ceil(degrees(acos((pow(c, 2) + pow(a, 2) - pow(b, 2)) / (2.0 * c * a))))

    if angle_a == 0 or angle_b == 0 or angle_c == 0: print 'n'
    elif angle_a == 90 or angle_b == 90 or angle_c == 90: print 'r'
    elif angle_a < 90 and angle_b < 90 and angle_c < 90: print 'a'
    elif angle_a > 90 or angle_b > 90 or angle_c > 90: print 'o'
except: print 'n'