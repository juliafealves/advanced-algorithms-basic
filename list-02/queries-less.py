# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Queries about less or equal elements


def binary_search(array, number, length):
    i, j = 0, length

    while abs(i - j) > 1:
        middle = (i + j) / 2

        if array[middle] > number:
            j = middle
        else:
            i = middle

    if i == 0 and array[i] > number:
        return 0
    elif j == length - 1 and array[j] < number:
        return length
    else:
        return j


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
    elif a[0] == a[-1] and sizes[0] > 1:
        if a[0] == number or number > a[-1]:
            visited[number] = sizes[0]
        elif number < a[-1]:
            visited[number] = 0

        output += str(visited[number]) + ' '
        continue
    else:
        visited[number] = binary_search(a, number, sizes[0])

    output += str(visited[number]) + ' '

print output.strip()


