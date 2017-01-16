# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name):
        self.name = name

print Student('Michael')


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print Student2('Michael')


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print n

f = Fib()
print f[0]
print f[1]
print f[2]
print f[3]
print f[10]
print f[100]
print f[0:5]
print f[:10]

print range(100)[5:10]


class Student3(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25

s3 = Student3()
print s3.name
print s3.score
print s3.age()


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list


class Student4(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print 'My name is %s.' % self.name

s4 = Student4('Michael')
s4()

print callable(Student4('Michael'))
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')
