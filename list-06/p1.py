# coding: utf-8

def dfs(v, visited, adjacent):
    visited[v] = True
    global count
    count += 1

    for neighbor in adjacent[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adjacent)

while True:
    try:
        n, m = map(int, raw_input().split())
        types = [[] for i in xrange(n+1)]
        count = 0

        for i in xrange(m):
            a, b = map(int, raw_input().split())
            types[a].append(b)
            types[b].append(a)

        e = int(raw_input())
        visited = [False] * (n + 1)
        dfs(e, visited, types)
        print count

    except EOFError: break