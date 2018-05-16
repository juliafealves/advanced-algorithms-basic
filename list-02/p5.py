# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: 239613
# Problem: Hours and Minutes - Ad-hoc

while True:
    try:
        angle = int(raw_input())
        if angle % 6 == 0:
            print "Y"
        else:
            print "N"
    except EOFError:
        break
