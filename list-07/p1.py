# coding: utf-8
from collections import defaultdict, Counter

def has_cycle(vertex):
    visited[vertex] = 1
    recusive_stack[vertex] = 1

    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            if has_cycle(neighbour): return True
        elif recusive_stack[neighbour] == 1: return True

    recusive_stack[vertex] = 0

    return False


t = int(raw_input())

for i in xrange(t):
    graph = defaultdict(list)
    visited = Counter()
    recusive_stack = Counter()
    is_cycle = False

    n, m = map(int, raw_input().split())

    for j in xrange(m):
        a, b = map(int, raw_input().split())
        graph[a].append(b)
        if a == b: is_cycle = True

    if not is_cycle:
        for vertex in xrange(1, n + 1):
            if not visited[vertex]:
                if has_cycle(vertex): is_cycle = True

    print 'SIM' if is_cycle else 'NAO'