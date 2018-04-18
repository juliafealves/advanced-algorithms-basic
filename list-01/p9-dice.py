# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Dice - AD-HOC - https://www.urionlinejudge.com.br/judge/en/problems/view/1342

config = map(int, raw_input().split())
count_players = config[0]
count_squares = config[1]

traps = map(int, raw_input().split())
count_throws = int(raw_input())

players = [[0]*count_throws for i in xrange(count_players)]
# players = [[0] * count_throws] * count_players

p = 0
i = 0

while i < count_throws:
    dices = map(int, raw_input().split())
    sum_dices = sum(dices)

    if sum(players[p]) > count_squares or sum_dices == 0:
        print '%i' % (p + 1)
        break

    if i != 0 and players[p][i-1] in traps:
        players[p][i] = 0
    else:
        players[p][i] = sum_dices

    if p == len(players) - 1:
        p = 0
        i += 1
    else:
        p += 1
