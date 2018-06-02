n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
dic = {}

j = 1
for i in a:
    if len(dic.keys()) == k: break

    try: dic[i]
    except: dic[i] = j

    j += 1

if len(dic.keys()) == k:
    print "YES"
    print ' '.join(map(str, dic.values()))
else: print "NO"