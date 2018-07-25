# coding: utf-8
q = int(raw_input())
handles = {}

for times in xrange(q):
    old, new = raw_input().split()

    found = False
    for older, newer in handles.iteritems():
        if old == newer:
            handles[older] = new
            found = True

    if not found:
        handles[old] = new

print len(handles)
for older, newer in handles.iteritems():
    print '%s %s' % (older, newer)