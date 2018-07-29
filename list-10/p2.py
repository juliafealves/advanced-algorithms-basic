# coding: utf-8
def dp():
    h, m = 0, 0

    for i in xrange(n):
        h = max(0, h + a[i])
        m = max(m, h)

    return m

while True:
    try:
        n = int(raw_input())
        per_day_cost = int(raw_input())
        a = []
        for _ in xrange(n):
            a.append(int(raw_input()) - per_day_cost)

        print dp()
    except EOFError: break