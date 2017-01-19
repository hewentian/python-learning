# -*- coding: utf-8 -*-
try:
    f = open('fileTest.txt', 'r')
    fr = f.read()
    print fr
finally:
    if f:
        f.close()

with open('fileTest.txt', 'r') as f:
    print f.read()

with open('fileTest.txt', 'r') as f:
    for line in f.readlines():
        print line.strip()

with open('picture.jpg', 'rb') as f:
    print f.read()

with open('fileTest.txt', 'rb') as f:
    print f.read().decode('gbk')

with open('fileTest.txt', 'w') as f:
    f.write('Hello, world.')
