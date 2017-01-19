# -*- coding: utf-8 -*-
import os

print os.name
#print os.uname()
print os.environ
print os.getenv('JAVA_HOME')
print os.path.abspath('.')

print os.path.join('d:\\', 'testdir')
os.mkdir('d:\\testdir')
os.rmdir('d:\\testdir')

print os.path.split('d:\\his.txt')
print os.path.splitext('d:\\his.txt')

os.rename('d:\\test.txt', 'd:\\test.py')
os.remove('d:\\test.py')

print [x for x in os.listdir('d:\\')]
print [x for x in os.listdir('d:\\') if os.path.isdir(x)]
print [x for x in os.listdir('d:\\') if os.path.isdir(x) and os.path.splitext(x)[1] == '.py']
