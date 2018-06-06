# coding: utf-8

def get_neighbors(i, j):
    neighbors = {}

    if j < b - 1 and adjacent[i][j + 1] == 1: neighbors[(i, j + 1)] = True
    if i < a - 1 and j < b - 1 and adjacent[i + 1][j + 1] == 1: neighbors[(i + 1, j + 1)] = True
    if i < a - 1 and adjacent[i + 1][j] == 1: neighbors[(i + 1, j)] = True
    if i < a - 1 and j > 0 and adjacent[i + 1][j - 1] == 1: neighbors[(i + 1, j - 1)] = True
    if j > 0 and adjacent[i][j - 1] == 1: neighbors[(i, j - 1)] = True
    if i > 0 and j > 0 and adjacent[i - 1][j - 1] == 1: neighbors[(i - 1, j - 1)] = True
    if i > 0 and adjacent[i - 1][j] == 1: neighbors[(i - 1, j)] = True
    if i > 0 and j < b - 1 and adjacent[i - 1][j + 1] == 1: neighbors[(i - 1, j + 1)] = True

    return neighbors


def is_children(vertex, children):
    try:
        children[vertex]
        return True
    except:
        return False


def is_parent(vertex, children):
    i, j = vertex

    if j < b - 1 and adjacent[i][j + 1] == 1 and not is_children((i, j + 1), children): return True
    if i < a - 1 and j < b - 1 and adjacent[i + 1][j + 1] == 1 and not is_children((i + 1, j + 1), children): return True
    if i < a - 1 and adjacent[i + 1][j] == 1 and not is_children((i + 1, j), children): return True
    if i < a - 1 and j > 0 and adjacent[i + 1][j - 1] == 1 and not is_children((i + 1, j - 1), children): return True
    if j > 0 and adjacent[i][j - 1] == 1 and not is_children((i, j - 1), children): return True
    if i > 0 and j > 0 and adjacent[i - 1][j - 1] == 1 and not is_children((i - 1, j - 1), children): return True
    if i > 0 and adjacent[i - 1][j] == 1 and not is_children((i - 1, j), children): return True
    if i > 0 and j < b - 1 and adjacent[i - 1][j + 1] == 1 and not is_children((i, j), children): return True

    return False

def get_parents(children):
    parents = {}

    for vertex in children.keys():
        i, j = vertex

        if is_parent(vertex, children): parents[(i, j)] = True
        else: adjacent[i][j] = 0

    return parents

def dfs(vertex):
    i, j = vertex
    neighbors = get_neighbors(i, j)
    neighbors[vertex] = True
    neighbors = get_parents(neighbors)
    adjacent[i][j] = 0

    global days

    for neighbor in neighbors.keys():
        x, y = neighbor

        if adjacent[x][y] == 1:
            days += 1
            dfs(neighbor)

t = int(raw_input())
visited = [[False] for i in xrange(101)] * 101

for i in xrange(t):
    adjacent = []
    days = 0
    a, b = map(int, raw_input().split())

    for j in xrange(a):
        adjacent.append(map(int, raw_input().split()))

    x, y = map(int, raw_input().split())
    dfs((x - 1, y - 1))
    print adjacent
    print days