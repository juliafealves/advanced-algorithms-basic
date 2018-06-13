# coding: utf-8
import sys
sys.setrecursionlimit(124751)

def get_parent(vertex):
    if parent[vertex] == vertex: return vertex
    parent[vertex] = get_parent(parent[vertex])

    return parent[vertex]

def union(u, v):
    xroot = get_parent(u)
    yroot = get_parent(v)

    if rank[xroot] < rank[yroot]: parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]: parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal():
    i, e, sum_path = 0, 0, 0
    g = sorted(graph)

    while e < n - 1:
        w, u, v = g[i]
        x = get_parent(u)
        y = get_parent(v)
        i += 1

        if x != y:
            e = e + 1
            sum_path += w
            union(x, y)

    return sum_path

graph = []
n, m = map(int, raw_input().split())
parent = range(n + 1)
rank = [0] * (n + 1)

for i in xrange(m):
    u, v, c = map(int, raw_input().split())
    graph.append((c, u, v))

print kruskal()