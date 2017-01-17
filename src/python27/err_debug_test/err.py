# -*- coding: utf-8 -*-
import logging

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'


try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'except:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'


class FooError(StandardError):
    pass


def foo(s):
   # return 10 / int(s)
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'
