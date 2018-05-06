# -*- coding: utf-8 -*-
assassins, dead = {}, []

while True:
    try:
        killer, murded = raw_input().split()
        dead.append(murded)

        try: assassins[killer] += 1
        except KeyError: assassins[killer] = 1
    except EOFError: break

assassins_set = set(assassins.keys())
dead = set(dead)
only_assassins = assassins_set.difference(dead)
only_assassins = list(only_assassins)
assassins_sorted = sorted(only_assassins)

print 'HALL OF MURDERERS'

for killer in assassins_sorted: print '%s %i' % (killer, assassins[killer])