# Problem: https://www.urionlinejudge.com.br/judge/pt/problems/view/2485
# -*- coding: utf-8 -*-
from Queue import Queue

queue = Queue()

def with_worms(x, y, vertex_parent):
    if adjacent[x][y] == 1:
        vertex_visited = (x, y)

        try: visited[vertex_visited]
        except KeyError:
            visited[vertex_visited] = True
            queue.put([vertex_visited, vertex_parent])

def bfs(adjacent):
    count = 0

    while not queue.empty():
        vertex = queue.get()
        x, y = vertex[0][0], vertex[0][1]
        vertex_parent = (x, y)
        parent = vertex[1]

        if x == 0 and y == 0:
            with_worms(x + 1, y + 1, vertex_parent)
            with_worms(x, y + 1, vertex_parent)
            with_worms(x + 1, y, vertex_parent)
        elif x == len(adjacent) - 1 and y == 0:
            with_worms(x - 1, y + 1, vertex_parent)
            with_worms(x, y + 1, vertex_parent)
            with_worms(x - 1, y, vertex_parent)
        elif x == len(adjacent) - 1 and y == len(adjacent[0]) - 1:
            with_worms(x - 1, y - 1, vertex_parent)
            with_worms(x, y - 1, vertex_parent)
            with_worms(x - 1, y, vertex_parent)
        elif x == 0 and y == len(adjacent[0]) - 1:
            with_worms(x + 1, y - 1, vertex_parent)
            with_worms(x + 1, y, vertex_parent)
            with_worms(x, y - 1, vertex_parent)
        elif x == 0:
            with_worms(x + 1, y, vertex_parent)
            with_worms(x + 1, y + 1, vertex_parent)
            with_worms(x + 1, y - 1, vertex_parent)
            with_worms(x, y + 1, vertex_parent)
            with_worms(x, y - 1, vertex_parent)
        elif y == 0:
            with_worms(x, y + 1, vertex_parent)
            with_worms(x - 1, y - 1, vertex_parent)
            with_worms(x + 1, y + 1, vertex_parent)
            with_worms(x - 1, y, vertex_parent)
            with_worms(x + 1, y, vertex_parent)
        elif y == len(adjacent[0]) - 1:
            with_worms(x, y - 1, vertex_parent)
            with_worms(x - 1, y - 1, vertex_parent)
            with_worms(x + 1, y - 1, vertex_parent)
            with_worms(x - 1, y, vertex_parent)
            with_worms(x + 1, y, vertex_parent)
        elif x == len(adjacent) - 1:
            with_worms(x - 1, y, vertex_parent)
            with_worms(x - 1, y + 1, vertex_parent)
            with_worms(x - 1, y - 1, vertex_parent)
            with_worms(x, y + 1, vertex_parent)
            with_worms(x, y - 1, vertex_parent)
        else:
            with_worms(x - 1, y - 1, vertex_parent)
            with_worms(x, y - 1, vertex_parent)
            with_worms(x + 1, y + 1, vertex_parent)
            with_worms(x + 1, y - 1, vertex_parent)
            with_worms(x, y + 1, vertex_parent)
            with_worms(x - 1, y + 1, vertex_parent)
            with_worms(x - 1, y, vertex_parent)
            with_worms(x + 1, y, vertex_parent)

        adjacent[x][y] = 'x'

        try: is_parent[parent]
        except KeyError:
            count += 1
            is_parent[parent] = True

    return count

t = int(raw_input())

for i in xrange(t):
    adjacent = []
    visited = {}
    is_parent = {}
    a, b = map(int, raw_input().split())

    for j in xrange(a):
        line = map(int, raw_input().split())
        adjacent.append(line)

    x, y = map(int, raw_input().split())
    queue.put([(x - 1, y - 1), (x - 1, y - 1)])
    print bfs(adjacent)
