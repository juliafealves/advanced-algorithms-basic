# -*- coding: utf-8 -*-
amount, before, after = map(int, raw_input().split())
initial = amount - before
if initial > after: print after + 1
else: print initial