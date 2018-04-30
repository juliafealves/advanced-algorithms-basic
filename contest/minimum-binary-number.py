# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: A. Minimum Binary Number


def truncate_one(number_binary, i, j):
    if j + 1 < len(number_binary):
        number_binary = number_binary[:i] + '1' + number_binary[j + 1:]
    else:
        number_binary = number_binary[:i] + '1'

    return number_binary


def swap_pair(number_binary, i, j):
    if j + 1 < len(number_binary):
        number_binary = number_binary[:i] + '10' + number_binary[j + 1:]
    else:
        number_binary = number_binary[:i] + '10'

    return number_binary


def verify(number_binary):
    i = 0
    j = i + 1

    while j < len(number_binary):
        if number_binary[i] == number_binary[j] == '1':
            number_binary = truncate_one(number_binary, i, j)
            i = 0
            j = i + 1
        elif number_binary[i] == '0' and number_binary[j] == '1':
            number_binary = swap_pair(number_binary, i, j)
            i = 0
            j = i + 1
        else:
            i += 1
            j += 1

    return number_binary


n = int(raw_input())
number_binary = raw_input()

if len(number_binary) > 1:
    print verify(number_binary)
else:
    print number_binary
