# -*- coding: utf-8 -*-
class Student(object):
    pass

s = Student()
s.name = 'Tim Ho'
print s.name


def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age

s2 = Student()
# s2.set_age(25)


def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
print s.score
s2.set_score(99)
print s2.score


class Student2(object):
    __slots__ = ('name', 'age')

s3 = Student2()
s3.name = 'Tim Ho'
s3.age = 25
#s3.score = 99
print s3.name
print s3.age
