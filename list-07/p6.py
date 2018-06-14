# coding: utf-8
def get_parent(vertex):
    if vertex == parent[vertex]: return parent[vertex]
    else:
        parent[vertex] = get_parent(parent[vertex])

        return parent[vertex]

def union(vertex1, vertex2):
    parent_1 = get_parent(vertex1)
    parent_2 = get_parent(vertex2)
    parent[parent_1] = parent_2

def is_some_parent(vertex1, vertex2):
    return get_parent(vertex1) == get_parent(vertex2)

n, m = map(int, raw_input().split())
parent = range(n + 1)

edge = 0
for i in xrange(m):
    x, y = map(int, raw_input().split())
    if not is_some_parent(x, y):
        edge += 1
        union(x, y)

print 1 * (2 ** (edge))