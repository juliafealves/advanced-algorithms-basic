# -*- coding: utf-8 -*-
GOOD = '.'
BAD = '-'
BLACK = 'B'
WHITE = 'W'

def set_adjacents(i, j):
    other_chessman = WHITE if chessboard[i][j] == BLACK else BLACK

    if j + 1 < len(chessboard[0]) and chessboard[i][j + 1] == GOOD:
        chessboard[i][j + 1] = other_chessman
        set_adjacents(i, j + 1)

    if i + 1 < len(chessboard) and chessboard[i + 1][j] == GOOD:
        chessboard[i + 1][j] = other_chessman
        set_adjacents(i + 1, j)

    if i - 1 >= 0 and chessboard[i - 1][j] == GOOD:
        chessboard[i - 1][j] = other_chessman
        set_adjacents(i - 1, j)

    if j - 1 >= 0 and chessboard[i][j - 1] == GOOD:
        chessboard[i][j - 1] = other_chessman
        set_adjacents(i, j - 1)

chessboard = []
n, m = map(int, raw_input().split())

for i in xrange(n):
    chessboard.append(list(raw_input()))

for i in xrange(n):
    for j in xrange(m):
        if chessboard[i][j] == GOOD:
            chessboard[i][j] = BLACK
            set_adjacents(i, j)

for line in chessboard:
    print ''.join(line)