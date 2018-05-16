# -*- coding: utf-8 -*-
# Author: Júlia Fernandes Alves. <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: A. Gravity Flip

columns = int(raw_input())
amount_cubes = map(int, raw_input().split())
cubes_gravity = map(str, sorted(amount_cubes))

print ' '.join(cubes_gravity)
