# -*- coding: utf-8 -*-
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

f = lambda x: x * x
print f(5)


def build(x, y):
    return lambda: x * x + y * y

f = build(2, 3)
print f()
