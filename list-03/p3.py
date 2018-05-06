# -*- coding: utf-8 -*-
from Queue import Queue
from Queue import PriorityQueue
from Queue import LifoQueue

def is_impossible(input, output):
    input, output = set(input), set(output)

    return len(output.difference(input)) > 0

while True:
    try:
        n = int(raw_input())
        queue = Queue(n)
        priority_queue = PriorityQueue(n)
        stack = LifoQueue(n)
        input, output = '', ''
        impossible = False
        is_queue = True
        is_stack = True
        is_priority_queue = True

        for times in xrange(n):
            operation, number = map(int, raw_input().split())

            if impossible: continue
            elif operation == 1:
                input += str(number)
                if is_queue: queue.put(number)
                if is_priority_queue: priority_queue.put((-number, number))
                if is_stack: stack.put(number)
            else:
                output += str(number)

                if len(output) > len(input) or is_impossible(input, output): impossible = True
                else:
                    if is_queue: is_queue = queue.get() == number
                    if is_stack: is_stack = stack.get() == number
                    if is_priority_queue: is_priority_queue = priority_queue.get()[1] == number

            if len(output) > len(input): impossible = True

        if impossible or len(output) == 0: print 'impossible'
        elif len(input) == len(output) == 1: print 'not sure'
        else:
            if (is_queue and is_priority_queue) or (is_queue and is_stack) or (is_priority_queue and is_stack): print 'not sure'
            elif is_queue: print 'queue'
            elif is_stack: print 'stack'
            elif is_priority_queue: print 'priority queue'
    except EOFError: break
