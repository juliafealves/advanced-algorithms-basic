# coding: utf-8
from Queue import PriorityQueue
from collections import defaultdict

def dijkstra(vertex):
    priority_queue = PriorityQueue()
    distance[vertex] = 0
    priority_queue.put((distance[1], vertex))

    while not priority_queue.empty():
        _, top = priority_queue.get()

        for neigbour, weight in graph[top]:
            if distance[neigbour] > distance[top] + weight:
                distance[neigbour] = distance[top] + weight
                priority_queue.put((distance[neigbour], neigbour))


INFINITY = 10000
t = int(raw_input())

for i in xrange(t):
    graph = defaultdict(list)
    v, k = map(int, raw_input().split())
    distance = [INFINITY] * (v + 1)

    for j in xrange(k):
        a, b, c = map(int, raw_input().split())
        graph[a].append((b, c))

    A, B = map(int, raw_input().split())
    dijkstra(A)
    print distance[B] if distance[B] != INFINITY else 'NO'