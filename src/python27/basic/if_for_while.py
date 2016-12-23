# -*- coding: utf-8 -*-
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
else:
    print 'your age is', age
    print 'teenager'

age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenage'
else:
    print 'kid'

if 'non null':
    print 'True'

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum1 = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum1 = sum1 + x;
print sum1

print range(5)

sum1 = 0
for x in range(101):
    sum1 = sum1 + x;
print sum1

sum1 = 0
n = 99
while n > 0:
    sum1 = sum1 + n
    n = n - 2
print sum1

birth = raw_input('birth:')
if birth < 2000:
    print '00前'
else:
    print '00后'

birth = int(raw_input('birth:'))
if birth < 2000:
    print '00前'
else:
    print '00后'
