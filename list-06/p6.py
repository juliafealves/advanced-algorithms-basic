# coding: utf-8
def order():
    i, j = 0, 1

    while j < len(s):
        if s == s_ordened: break

        if s[i] == 'B' and s[j] == 'G':
            s[i], s[j] = s[j], s[i]
            i = j + 1
            j = i + 1
        else:
            i += 1
            j += 1

n, t = map(int, raw_input().split())
s = list(raw_input())
s_ordened = sorted(s, reverse=True)

for i in xrange(t): order()

print ''.join(s)