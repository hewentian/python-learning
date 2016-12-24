# -*- coding: utf-8 -*-
L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
for n in g:
    print n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

fib(6)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

o = fib2(6)
print o.next()
print o.next()
print o.next()

for n in fib2(6):
    print n


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

for n in odd():
    print n
