# coding: utf-8
notes = {1: 'do', 2: 'do#', 3: 're', 4: 're#', 5: 'mi', 6: 'fa', 7: 'fa#', 8: 'sol', 9: 'sol#', 10: 'la', 11: 'la#', 12: 'si'}
gaps = [
    [1, 3, 5, 6, 8, 10, 12],
    [1, 2, 4, 6, 7, 9, 11],
    [2, 3, 5, 7, 8, 10, 12],
    [1, 3, 4, 6, 8, 9, 11],
    [2, 4, 5, 7, 9, 10, 12],
    [1, 3, 5, 6, 8, 10, 11],
    [2, 4, 6, 7, 9, 11, 12],
    [1, 3, 5, 7, 8, 10, 12],
    [1, 2, 4, 6, 8, 9, 11],
    [2, 3, 5, 7, 9, 10, 12],
    [1, 3, 4, 6, 8, 10, 11],
    [2, 4, 5, 7, 9, 11, 12]
]

n = int(raw_input())
nts = set()

for _ in xrange(n):
    nt = int(raw_input())
    if nt > 12: nt %= 12

    nts.add(nt)

nts = list(nts)
nts.sort()

i, j, a = 0, 0, 0
while True:
    if a == len(nts) or i == 12: break
    if nts[j] in gaps[i]:
        a += 1
        if j < len(nts): j += 1
    else:
        if i < len(gaps): i += 1
        j = 0
        a = 0

if a == 0: print 'desafinado'
else: print notes[i + 1]
