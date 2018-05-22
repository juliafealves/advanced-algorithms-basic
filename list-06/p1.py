# Problem: https://www.urionlinejudge.com.br/judge/pt/problems/view/2562
# -*- coding: utf-8 -*-
def dfs(v, visited, adjacent, count):
    visited[v] = True
    count += 1

    for neighbor in adjacent[v]:
        if not visited[neighbor]:
            return dfs(neighbor, visited, adjacent, count)

    return count

while True:
    try:
        n, m = map(int, raw_input().split())
        types = [[] for i in xrange(n+1)]

        for i in xrange(m):
            a, b = map(int, raw_input().split())
            types[a].append(b)
            types[b].append(a)

        e = int(raw_input())
        visited = [False] * (n + 1)
        print dfs(e, visited, types, 0)
    except EOFError: break