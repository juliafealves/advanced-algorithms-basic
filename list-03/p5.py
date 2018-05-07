# -*- coding: utf-8 -*-
from Queue import Queue
from Queue import LifoQueue

while True:
    try:
        string = raw_input()
        queue = Queue(len(string))
        stack = LifoQueue(len(string))
        new_string = ''

        i = len(string) - 1

        while i >= 0:
            if string[i] != '[' and string[i] != ']': new_string = string[i] + new_string[:]
            elif string[i] == ']':
                stack.put(new_string)
                new_string = ''
            elif string[i] == '[':
                queue.put(new_string)
                new_string = ''

            i -= 1

        string = ''

        while not queue.empty(): string += queue.get()
        string += new_string
        while not stack.empty(): string += stack.get()

        print string
    except EOFError: break