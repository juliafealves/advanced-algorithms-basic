# -*- coding: utf-8 -*-

def binary_search(list, number):
    i, j = 0, len(list)

    while i <= j:
        middle = (i + j) / 2

        if list[middle] == number:
            if middle > 0 and list[middle - 1] == number:
                middle -= 1

                while numbers[middle] == number:
                    middle -= 1

                return middle + 1

            return middle
        elif list[middle] > number:
            j = middle - 1
        else:
            i = middle + 1

    return -1

count = 1

while True:
    n, q = map(int, raw_input().split())

    if n == 0 and q == 0:
        break

    numbers = []
    not_found = []
    found = {}

    for times in xrange(n):
        numbers.append(int(raw_input()))

    numbers = sorted(numbers)

    print "CASE# %i:" % count

    for times in xrange(q):
        number = int(raw_input())

        if number < numbers[0] or number > numbers[-1]:
            print "%i not found" % number
        elif numbers[0] == number:
            print "%i found at %i" % (number, 1)
        elif number in not_found:
            print "%i not found" % number
        elif numbers[-1] == number:
            position = len(numbers) - 1

            if position > 0 and numbers[position - 1] == number:
                position -= 1

                while numbers[position] == number:
                    position -= 1

                position += 1

            found[number] = position + 1
            print "%i found at %i" % (number, position + 1)
        else:
            try:
                print "%i found at %i" % (number, found[number])
            except KeyError:
                position = binary_search(numbers, number)

                if position == -1:
                    not_found.append(number)
                    print "%i not found" % number
                else:
                    found[number] = position + 1
                    print "%i found at %i" % (number, position + 1)

    count += 1