# coding: utf-8
import sys
sys.setrecursionlimit(100001)
def get_parent(vertex):
    if vertex == parent[vertex]: return parent[vertex]
    else:
        parent[vertex] = get_parent(parent[vertex])
        return parent[vertex]

def is_some_parent(vertex1, vertex2):
    return get_parent(vertex1) == get_parent(vertex2)

def union(vertex1, vertex2):
    parent_1 = get_parent(vertex1)
    parent_2 = get_parent(vertex2)
    parent[parent_1] = parent_2

n, k = map(int, raw_input().split())
parent = range(n + 1)

for i in xrange(k):
    o, a, b = raw_input().split()
    a = int(a)
    b = int(b)

    if o == 'C': print 'S' if is_some_parent(a, b) else 'N'
    if o == 'F': union(a, b)
