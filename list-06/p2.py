from Queue import Queue

queue = Queue()

def bfs(adjacent):
    count = 0
    parent_before = (-1, -1)
    visited = {}

    while not queue.empty():
        vertex = queue.get()
        x, y = vertex[0][0], vertex[0][1]
        vertex_parent = str(x) + str(y)
        parent = vertex[1]

        if y + 1 < len(adjacent[0]) and adjacent[x][y + 1] == 1:
            vertex = str(x) + str(y + 1)

            try: visited[vertex]
            except ValueError:
                visited[vertex] = True
                queue.put((vertex, vertex_parent))

        if x + 1 < len(adjacent) and y + 1 < len(adjacent[0]) and adjacent[x + 1][y + 1] == 1:
            queue.put([(x + 1, y + 1), (x, y)])

        if x + 1 < len(adjacent) and adjacent[x + 1][y] == 1:
            queue.put([(x + 1, y), (x, y)])

        if y - 1 >= 0 and adjacent[x][y - 1] == 1:
            queue.put([(x, y - 1), (x, y)])

        if x - 1 >= 0 and y - 1 >= 0 and adjacent[x - 1][y - 1] == 1:
            queue.put([(x - 1, y - 1), (x, y)])

        if x - 1 >= 0 and adjacent[x - 1][y] == 1:
            queue.put([(x - 1, y), (x, y)])

        if x - 1 >= 0 and y + 1 < len(adjacent[0]) and adjacent[x - 1][y + 1] == 1:
            queue.put([(x - 1, y + 1), (x, y)])

        if x + 1 < len(adjacent) and y - 1 >= 0 and adjacent[x + 1][y - 1] == 1:
            queue.put([(x + 1, y - 1), (x, y)])

        adjacent[x][y] = 'x'

        if parent_before != parent:
            count += 1
            parent_before = parent

    print count
    print queue.queue
    print adjacent

t = int(raw_input())
for i in xrange(t):
    adjacent = []
    a, b = map(int, raw_input().split())

    for j in xrange(a):
        line = map(int, raw_input().split())
        adjacent.append(line)

    x, y = map(int, raw_input().split())
    queue.put([(x - 1, y - 1), (x - 1, y - 1)])
    bfs(adjacent)
