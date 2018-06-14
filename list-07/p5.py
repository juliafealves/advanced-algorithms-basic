# coding: utf-8
from Queue import PriorityQueue
from collections import defaultdict, Counter
INFINITY = 1000000

def dijkstra(vertex, graph):
    priority_queue = PriorityQueue()
    distance[vertex] = 0
    priority_queue.put((distance[1], vertex))

    while not priority_queue.empty():
        _, top = priority_queue.get()

        for neigbour, weight in graph[top]:
            if distance[neigbour] > distance[top] + weight:
                distance[neigbour] = distance[top] + weight
                priority_queue.put((distance[neigbour], neigbour))
                parents[neigbour] = top

graph = defaultdict(list)
n, m = map(int, raw_input().split())
distance = [INFINITY] * (n + 1)
visited = Counter()

for i in xrange(m):
    a, b, w = map(int, raw_input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

parents = [0] * (n + 1)
parents[1] = -1
dijkstra(1, graph)

if distance[n] == INFINITY: print '-1'
else:
    path, v = '', n

    while v != -1:
        path = ' ' + str(v) + path
        v = parents[v]

    print path.strip()

