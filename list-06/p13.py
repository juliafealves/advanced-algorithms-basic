# coding: utf-8
from collections import defaultdict
from collections import Counter
from Queue import Queue

def dfs(parent):
    global push
    push += 1
    visited[parent] = 1

    for children in graph[parent]:
        if children == n: break
        elif children > m: continue
        elif not visited[children]: dfs(children)


def create_graph(destiny):
    deph = 0

    while not queue.empty():
        vertex = queue.get()
        visited[vertex] = deph
        deph += 1

        vertex_red = vertex * 2
        vertex_blue = vertex - 1

        if vertex_red <= (m + m/2) and not visited[vertex_red]:
            visited[vertex_red] = deph
            graph[vertex].append(vertex_red)
            queue.put(vertex_red)

        if vertex_blue > 0 and not visited[vertex_blue]:
            visited[vertex_blue] = deph
            graph[vertex].append(vertex_blue)
            queue.put(vertex_blue)

        if vertex_red == destiny or vertex_blue == destiny:
            break


n, m = map(int, raw_input().split())

if n == m: print 0
elif n < m:
    graph = defaultdict(list)
    queue = Queue()
    visited = Counter()
    push = 0

    queue.put(n)
    create_graph(m)
    print graph.items()
    print visited
    print push
else: print n - m