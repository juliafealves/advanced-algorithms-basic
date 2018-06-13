# coding: utf-8
from collections import defaultdict, Counter
from Queue import Queue
INFINITY = 5000

def bfs(vertex):
    queue = Queue()
    distance[vertex] = 0
    queue.put(vertex)

    while not queue.empty():
        top = queue.get()
        for neigbour in graph[top]:
            if not distance.has_key(neigbour): distance[neigbour] = INFINITY
            if distance[neigbour] > distance[top] + 1:
                distance[neigbour] = distance[top] + 1
                queue.put(neigbour)

distance = Counter()
graph = defaultdict(list)

p, l = map(int, raw_input().split())
for i in xrange(l):
    a, b = raw_input().split()
    graph[a].append(b)
    graph[b].append(a)

total_distance = 0
bfs('Entrada')
total_distance += distance['*']
distance = Counter()
bfs('*')
total_distance += distance['Saida']

print total_distance