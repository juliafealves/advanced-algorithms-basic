# coding: utf-8
n = int(raw_input())
a = map(int, raw_input().split())

for an in a:
    if an == 1:
        print '-1'
        exit()

print 1