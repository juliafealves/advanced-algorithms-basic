# coding: utf-8
from Queue import PriorityQueue
from collections import defaultdict

def get_path(vertex, source, visited, adjacent):
    visited[vertex] = True
    path.append(vertex)

    if source == vertex: print path
    else:
        for neighbor in adjacent[vertex]:
            if not visited[neighbor]: get_path(neighbor, source, visited, adjacent)

def dijkstra(vertex):
    new_graph = defaultdict(list)
    priority_queue = PriorityQueue()
    distance[vertex] = 0
    priority_queue.put((distance[1], vertex))

    while not priority_queue.empty():
        _, top = priority_queue.get()

        for neigbour, weight in graph[top]:
            if distance[neigbour] > distance[top] + weight:
                new_graph[neigbour].append(top)
                distance[neigbour] = distance[top] + weight
                priority_queue.put((distance[neigbour], neigbour))

    return new_graph

INFINITY = 1000000
graph = defaultdict(list)
n, m = map(int, raw_input().split())
distance = [INFINITY] * (n + 1)


for i in xrange(m):
    a, b, w = map(int, raw_input().split())
    graph[a].append((b, w))

print graph
new_graph = dijkstra(1)
print new_graph
visited = [False] * (n + 1)
path = []


if distance[n] == INFINITY: print '-1'
else: get_path(1, n, visited, new_graph)
