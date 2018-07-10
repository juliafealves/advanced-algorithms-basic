# coding: utf-8
notes = {1: 'do', 2: 'do#', 3: 're', 4: 're#', 5: 'mi', 6: 'fa', 7: 'fa#', 8: 'sol', 9: 'sol#', 10: 'la', 11: 'la#', 12: 'si'}
gap = {1: 2, 3: 2, 5: 1, 6: 2, 8: 2, 10: 2, 12: 1}
gaph = {1: 1, 2: 2, 4: 2, 6: 1, 7: 2, 8: 2, 11: 2}

n = int(raw_input())

b = int(raw_input())

for _ in xrange(n - 1):
    a = int(raw_input())

    if b % 12 == 0:
   
