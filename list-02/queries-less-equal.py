# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Queries about less or equal elements


def binary_search(array, number, length):
    i, j = 0, length

    while abs(i - j) > 1:
        middle = (i + j) // 2

        if array[middle] > number:
            j = middle
        else:
            i = middle

    return j


sizes_array = map(int, raw_input().split())
array_a = map(int, raw_input().split())
array_b = map(int, raw_input().split())
array_sorted = sorted(array_a)
visited = {}
output = ''

for number in array_b:
    if number in visited.keys():
        output += str(visited[number]) + ' '
        continue
    else:
        amount = binary_search(array_sorted, number, sizes_array[0])
        if array_sorted[amount - 1] > number:
            amount -= 1

        visited[number] = amount

    output += str(visited[number]) + ' '

print output.strip()
