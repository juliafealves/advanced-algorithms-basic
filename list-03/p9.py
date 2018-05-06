# -*- coding: utf-8 -*-
n = int(raw_input())

for times in xrange(n):
    expression = raw_input()
    parts_diamond = ''
    diamonds = 0

    for char in expression:
        if char == '<': parts_diamond += char
        if char == '>': parts_diamond += char

    if len(parts_diamond) > 0:
        i = 0

        while i < len(parts_diamond) - 1:
            if parts_diamond[i] == '<' and parts_diamond[i + 1] == '>':
                parts_diamond = parts_diamond[:i] + parts_diamond[i + 2:]
                diamonds += 1
                i = 0
            else:
                i += 1


    print diamonds