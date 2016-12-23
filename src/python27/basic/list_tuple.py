# -*- coding: utf-8 -*-
classmate = ['Michael', 'Bob', 'Tracy']
print classmate
print len(classmate)
print classmate[0]
print classmate[1]
print classmate[2]
# print classmate[3]
print classmate[-1]
print classmate[-2]
print classmate[-3]
# print classmate[-4]

classmate.append('Adam')
print classmate
classmate.insert(1, 'Jack')
print classmate

classmate.pop()
print classmate

classmate.pop(1)
print classmate

classmate[1] = 'sarah'
print classmate

L = ['Apple', 123, True]
print L

s = ['python', 'java', ['asp', 'php'], 'schema']
print s
print len(s)

p = ['asp', 'php']
s = ['python', 'java', p, 'schema']
print s
print s[2][1]

L = []
print len(L)


# below show the usage of tuple
classmate = ('Michael', 'Bob', 'Tracy')
print classmate
print classmate[0]
print classmate[-1]

t = ()
print t

t2 = (1)
print t2

t3 = (1,)
print t3

t4 = ('a', 'b', ['A', 'B'])
t4[2][0] = 'X'
t4[2][1] = 'Y'
print t4

t5 = ['A', 'B']
t6 = ('a', 'b', t5)
print t6
t5.append('C')
print t6
