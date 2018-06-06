# coding: utf-8
from collections import defaultdict
from collections import Counter
from Queue import Queue

def create_graph(source):
    while not queue.empty():
        vertex = queue.get()
        vertex_red = vertex * 2
        vertex_blue = vertex - 1

        if vertex_red <= (source * 2) and not visited[vertex_red]:
            visited[vertex_red] = visited[vertex] + 1
            queue.put(vertex_red)

        if vertex_blue > 0 and not visited[vertex_blue]:
            visited[vertex_blue] = visited[vertex] + 1
            queue.put(vertex_blue)

        if vertex_red == source or vertex_blue == source:
            return visited[source]

n, m = map(int, raw_input().split())

if n == m: print 0
elif n < m:
    queue = Queue()
    visited = Counter()
    graph = defaultdict(list)

    visited[n] = 0
    queue.put(n)
    print create_graph(m)
else: print n - m
