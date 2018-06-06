# coding: utf-8
from collections import defaultdict, Counter

def dfs(vertex):
    visited[vertex] = 1
    global total
    total += 1

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(neighbor)


n, m = map(int, raw_input().split())
graph = defaultdict(list)
visited = Counter()
first, total = 0, 0

for i in xrange(m):
    u, v = map(int, raw_input().split())
    if first == 0: first = u

    graph[u].append(v)
    graph[v].append(u)

if m != n - 1 or n == 1: print 'NO'
else:
    dfs(first)
    print 'YES' if total == n else 'NO'