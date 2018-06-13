# coding: utf-8
def count_opinion(opinion):
    global negative_opinion
    if opinion == '1': negative_opinion += 1

negative_opinion = 0

q = int(raw_input())
opinions = map(count_opinion, raw_input().split())

positive_opinion = abs(q - negative_opinion)

print 'N' if positive_opinion <= negative_opinion else 'Y'