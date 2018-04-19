# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Dice - AD-HOC

while True:
    game = map(int, raw_input().split())

    if game[0] == game[1] == 0:
        break

    traps = map(int, raw_input().split())
    throws = int(raw_input())

    squares = game[1]
    players = [0] * game[0]
    blockeds = [0] * game[0]

    p = 0
    i = 0

    while i < throws:
        if blockeds[p] == 1:
            blockeds[p] = 0
            p += 1

            if p >= len(players):
                p = 0
            continue

        dices = sum(map(int, raw_input().split()))
        players[p] += dices

        if players[p] in traps:
            blockeds[p] = 1

        if players[p] > squares:
            print '%i' % (p + 1)
            break

        if p == len(players) - 1:
            p = 0
        else:
            p += 1

        i += 1
