# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Queries about less or equal elements


def binary_search(array, number, i, j):
    while abs(i - j) > 1:
        middle = (i + j) // 2

        if array[middle] > number:
            j = middle
        else:
            i = middle

    return j


def higher_index(dictionary, number, length):
    higher = max(dictionary.keys())

    return dictionary[higher] if higher > number else (length - 1)


def lower_index(dictionary, number):
    lower = min(dictionary.keys())

    return dictionary[lower] if lower < number else 0


sizes_array = map(int, raw_input().split())
array_a = map(int, raw_input().split())
array_b = map(int, raw_input().split())
array_sorted = sorted(array_a)
visited = {}
output = ''
initial = 0
end = sizes_array[0] - 1

higher_all = max(array_b)

for i in xrange(len(array_b)):
    number = array_b[i]

    if number in visited.keys():
        output += str(visited[number]) + ' '
        continue
    else:
        if higher_all != number:
            if i != 0:
                initial = lower_index(visited, number)
                end = higher_index(visited, number, sizes_array[0])

            amount = binary_search(array_sorted, number, initial, end)

            if array_sorted[amount - 1] > number and amount > 0:
                amount -= 1
        else:
            amount = visited[max(visited.keys())] + 1

        visited[number] = amount

    output += str(visited[number]) + ' '

print output.strip()
