# -*- coding: utf-8 -*-
while True:
    try:
        expression = raw_input()
        parenthesis = ''
        open = 0
        close = 0

        first = False

        for char in expression:
            if char == '(':
                if not first: first = True

                parenthesis += char
                open += 1
            elif char == ')':
                if not first:
                    print 'incorrect'
                    break

                parenthesis += char
                close += 1

        if len(parenthesis) > 0:
            if parenthesis[-1] == '(': print 'incorrect'
            elif open != close != 0: print 'incorrect'
            else: print 'correct'
    except EOFError:
        break