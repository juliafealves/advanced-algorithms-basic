# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Queries about less or equal elements


def binary_search(array, number, length):
    i, j = 0, length

    while i < j:
        middle = (i + j) / 2

        if array[middle] > number:
            j = middle - 1
        else:
            i = middle + 1

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


