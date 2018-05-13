# -*- coding: utf-8 -*-
query = int(raw_input())
possible_result = [1, 7, 9, 3]

for q in xrange(query):
    pow = int(raw_input())
    print possible_result[pow % 4]