# coding: utf-8
n = int(raw_input())
lr = True
board = ''

for i in xrange(n):
    if lr:
        board += raw_input()
        lr = False
    else:
        board += raw_input()[::-1]
        lr = True

food = 0
max_food = food

for f in board:
    if f == 'o': food += 1
    elif f == 'A':
        if food > max_food: max_food = food
        food = 0

if food > max_food: max_food = food
print max_food