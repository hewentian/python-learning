# -*- coding: utf-8 -*-


class Student1(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an inteter')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s1 = Student1()
s1.set_score(60)
print s1.get_score()
#s1.set_score(9999)


class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an inteter')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s2 = Student2()
s2.score = 60
print s2.score
#s2.score = 9999


class Student3(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth

s3 = Student3()
s3.birth = 1989
print s3.birth
print s3.age
