# coding: utf-8
n, m = map(int, raw_input().split())
car = {}

for i in xrange(n):
    time = sum(map(int, raw_input().split()))
    car[time] = i + 1

rank = sorted(car.keys())

for p in rank[:3]: print car[p]