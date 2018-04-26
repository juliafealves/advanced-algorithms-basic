# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Queries about less or equal elements


def position_lower(array, index, number, length):
    while True:
        if index == length - 1 or array[index + 1] > number:
            return index + 1
        else:
            index += 1


def binary_search(array, number, length):
    i, j = 0, length

    while i < j:
        middle = (i + j) / 2

        if array[middle] > number:
            j = middle - 1
        else:
            return position_lower(array, middle, number, length)
    return j + 1


sizes = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
a = sorted(a)
visited = {}
output = ''

for number in b:
    if number in visited.keys():
        output += str(visited[number]) + ' '
        continue
    elif a[0] > number:
        visited[number] = 0
    elif a[-1] <= number:
        visited[number] = sizes[0]
    else:
        visited[number] = binary_search(a, number, sizes[0])

    output += str(visited[number]) + ' '

print output.strip()