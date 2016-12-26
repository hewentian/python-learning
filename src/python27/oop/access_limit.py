# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

bart.age = 20
print bart.age

print bart.get_score()
bart.set_score(90)
print bart.get_score()

print bart.get_grade()
print lisa.get_grade()

# bart.set_score(-1)
# print bart.get_score()

print bart._Student__name
