# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Queries about less or equal elements


def binary_search(array, number, length):
    i, j = 0, length

    while i <= j:
        middle = (i + j) / 2

        if array[middle] > number:
            if middle - 1 >= 0 and array[middle - 1] <= number:
                return middle

            j = middle - 1
        else:
            if middle + 1 < length and array[middle + 1] > number:
                return middle + 1

            i = middle + 1


sizes = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
a = sorted(a)
output = ''

for number in b:
    if a[0] > number:
        valor = 0
    elif a[-1] <= number:
        valor = sizes[0]
    else:
        valor = binary_search(a, number, sizes[0])

    output += str(valor) + ' '

print output.strip()
