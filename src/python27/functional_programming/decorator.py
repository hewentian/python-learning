# -*- coding: utf-8 -*-
import functools


def now():
    print '2013-12-25'

f = now
f()

print now.__name__


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now2():
    print '2013-12-25'

now2()
print now2.__name__

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('execute')
def now3():
    print '2013-12-25'

now3()
print now3.__name__
