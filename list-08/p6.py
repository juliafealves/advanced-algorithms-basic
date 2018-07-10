# coding: utf-8


def get_subsequence(string):
    for i in xrange(len(string)):
        for j in xrange(len(string), -1, -1):
            substring = string[i:j]

            if substring != '': subsequences.add(substring)

            for k in xrange(1, len(substring) - 1):
                substring = substring[k:]

                if substring != '': subsequences.add(substring)

                get_subsequence(substring)



subsequences = set()

get_subsequence('abc')
print subsequences