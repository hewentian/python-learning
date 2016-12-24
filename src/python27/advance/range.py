# -*- coding: utf-8 -*-
print range(1, 11)

L = []
for x in range(1, 11):
    L.append(x * x)
print L

L = [x * x for x in range(1, 11)]
print L

L = [x * x for x in range(1, 11) if x % 2 == 0]
print L

L = [m + n for m in 'ABC' for n in 'XYZ']
print L

import os
print [d for d in os.listdir('.')]

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.iteritems():
    print k, '=', v

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]
