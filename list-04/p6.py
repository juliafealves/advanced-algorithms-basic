# -*- coding: utf-8 -*-
from math import factorial

def gdc_factorial(number1, number2):
    return factorial(min(number1, number2))

a, b = map(int, raw_input().split())
print gdc_factorial(a, b)