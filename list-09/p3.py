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


MAX = 31

while True:
    try:
        memo = [[-1 for _ in xrange(MAX)] for _ in xrange(MAX)]
        weights, values = [], []
        size = 0

        query = int(raw_input())

        if query == 0: break

        capacity = int(raw_input())

        for _ in xrange(query):
            v, w = map(int, raw_input().split())
            weights.append(w)
            values.append(v)
            size = query

        print "%i min." % knapsack(0, capacity)

    except EOFError: break