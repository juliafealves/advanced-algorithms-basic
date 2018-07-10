# coding: utf-8

def knapsack(item, capacity):
    if memo[item][capacity] >= 0: return memo[item][capacity]

    if item == size or capacity <= 0:
        memo[item][capacity] = 0

        return memo[item][capacity]

    not_put = knapsack(item + 1, capacity)

    if weights[item] <= capacity:
        put = values[item] + knapsack(item + 1, capacity - weights[item])
        memo[item][capacity] = max(not_put, put)

        return memo[item][capacity]

    memo[item][capacity] = not_put

    return memo[item][capacity]

MAX = 101
query = int(raw_input())

for _ in xrange(query):
    memo = [[-1 for _ in xrange(MAX)] for _ in xrange(MAX)]
    weights, values = [], []

    size = int(raw_input())

    for _ in xrange(size):
        v, w = map(int, raw_input().split())
        values.append(v)
        weights.append(w)

    capacity = int(raw_input())
    resistance = int(raw_input())
    fire = knapsack(0, capacity)

    if fire >= resistance: print 'Missao completada com sucesso'
    else: print 'Falha na missao'