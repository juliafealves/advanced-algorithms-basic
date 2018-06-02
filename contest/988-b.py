def is_substring(string):
    try: dic_substrings[len(string)].append(string)
    except:
        dic_substrings[len(string)] = []
        dic_substrings[len(string)].append(string)

    for s in substrings:
        if len(s) <= len(string) and string.find(s) == -1: return False
        elif len(s) > len(string) and s.find(string) == -1: return False

    return True

n = int(raw_input())
dic_substrings = {}
substrings = []
no_substring = False

substring = raw_input()
dic_substrings[len(substring)] = []
dic_substrings[len(substring)].append(substring)
substrings.append(substring)

for i in xrange(n - 1):
    substring = raw_input()
    substrings.append(substring)

    if not no_substring:
        no_substring = not is_substring(substring)

if no_substring: print "NO"
else:
    print "YES"

    indexes = sorted(dic_substrings.keys())

    for i in indexes:
        strings = sorted(dic_substrings[i])

        print '\n'.join(strings)