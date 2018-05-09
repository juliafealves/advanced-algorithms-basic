# -*- coding: utf-8 -*-
from collections import deque

queries = int(raw_input())
queue = deque()
is_reversed = False
index = 0

for q in xrange(queries):
    operation = raw_input()

    if operation.find('toFront') != -1:
        element = operation.split()[1]
        if is_reversed: queue.append(element)
        else: queue.appendleft(element)
    elif operation.find('push_back') != -1:
        element = operation.split()[1]
        if not is_reversed: queue.append(element)
        else: queue.appendleft(element)
    elif operation == 'front':
        if len(queue) > 0:
            if is_reversed: print queue.pop()
            else: print queue.popleft()
        else:
            print 'No job for Ada?'
    elif operation == 'back':
        if len(queue) > 0:
            if is_reversed: print queue.popleft()
            else: print queue.pop()
        else:
            print 'No job for Ada?'
    elif operation == 'reverse': is_reversed = True if not is_reversed else False