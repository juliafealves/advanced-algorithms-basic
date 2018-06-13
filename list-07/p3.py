# coding: utf-8

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
    i, e = 0, 0
    g = sorted(graph)

    while e < n - 1:
        w, u, v = g[i]
        x = get_parent(u)
        y = get_parent(v)
        i += 1

        if x != y:
            e = e + 1
            if u < v: print "%s %s" % (u, v)
            else: print "%s %s" % (v, u)
            union(x, y)

t = 1

while True:
    graph = []
    n, m = map(int, raw_input().split())
    parent = range(n + 1)
    rank = [0] * (n + 1)

    if n == m == 0: break
    print 'Teste %d' % t

    for i in xrange(m):
        u, v, w = map(int, raw_input().split())
        graph.append((w, u, v))

    kruskal()
    t += 1
