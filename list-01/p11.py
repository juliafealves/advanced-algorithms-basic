# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Division of Nlogonia - AD-HOC

while True:
    inputs = int(raw_input())

    if inputs == 0:
        break

    division = map(int, raw_input().split())

    for i in xrange(inputs):
        coordinates = map(int, raw_input().split())

        if coordinates[0] in division or coordinates[1] in division:
            print "divisa"
        elif coordinates[0] > division[0] and coordinates[1] > division[1]:
            print "NE"
        elif coordinates[0] > division[0] and coordinates[1] < division[1]:
            print "SE"
        elif coordinates[0] < division[0] and coordinates[1] > division[1]:
            print "NO"
        else:
            print "SO"
