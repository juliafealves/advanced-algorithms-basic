# coding: utf-8
from collections import defaultdict
from collections import Counter
from Queue import Queue

def get_children(vertex):
    i, j = vertex
    children = []

    child = (i, j + 1)
    if j < b - 1 and not visited.has_key(child) and adjacent[i][j + 1] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    child = (i + 1, j + 1)
    if i < a - 1 and not visited.has_key(child) and j < b - 1 and adjacent[i + 1][j + 1] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    child = (i + 1, j)
    if i < a - 1 and not visited.has_key(child) and adjacent[i + 1][j] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    child = (i + 1, j - 1)
    if i < a - 1 and j > 0 and not visited.has_key(child) and adjacent[i + 1][j - 1] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    child = (i, j - 1)
    if j > 0 and not visited.has_key(child) and adjacent[i][j - 1] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    child = (i - 1, j - 1)
    if i > 0 and j > 0 and not visited.has_key(child) and adjacent[i - 1][j - 1] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    child = (i - 1, j)
    if i > 0 and not visited.has_key(child) and adjacent[i - 1][j] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    child = (i - 1, j + 1)
    if i > 0 and j < b - 1 and not visited.has_key(child) and adjacent[i - 1][j + 1] == 1:
        children.append(child)
        visited[child] = visited[vertex] + 1
        queue.put(child)

    return children

def count_days():
    while not queue.empty():
        vertex = queue.get()
        graph[vertex] = get_children(vertex)


q = int(raw_input())
for i in xrange(q):
    a, b = map(int, raw_input().split())
    adjacent = []

    for j in xrange(a): adjacent.append(map(int, raw_input().split()))

    x, y = map(int, raw_input().split())
    queue = Queue()
    visited = Counter()
    graph = defaultdict(list)

    vertex = (x - 1, y - 1)
    queue.put(vertex)
    visited[vertex] = 0
    count_days()

    print max(visited.values())