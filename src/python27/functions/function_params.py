# -*- coding: utf-8 -*-
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5)
print power(5, 3)


def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Ada', 'M', city='Tianjin')


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])

print add_end()
print add_end()


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1, 2, 3])
print calc((1, 3, 5, 7))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc2(1, 2, 3)
print calc2(1, 3, 5, 7)
print calc2(0)

nums = [1, 2, 3]
print calc2(nums[0], nums[1], nums[2])
print calc2(*nums)


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)


def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4)
kw = {'x':99}
func(*args, **kw)
