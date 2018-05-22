from Queue import Queue

def bfs(x, y, listAdjacent):
    queue = Queue()
    vertex = listAdjacent[x][y]

    for i in xrange(x, len(listAdjacent[x])):
        for j in xrange(y, len(listAdjacent[y])):
            if (i + 1 < len(listAdjacent[0] and listAdjacent[x][y+1] == 1):
                queue.put((x, y + 1))



listAdjacent = [[0]]

t = int(raw_input())
for i in xrange(t):
    a, b = map(int, raw_input().split())

    for j in xrange(a):
        line = map(int, raw_input().split())
        listAdjacent.append(line)

    x, y = map(int, raw_input().split())
    bfs(x, y, listAdjacent)
