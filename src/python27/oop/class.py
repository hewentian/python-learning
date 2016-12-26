# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

bart.age = 20
print bart.age

print bart.score
bart.score = 90
print bart.score

print bart.get_grade()
print lisa.get_grade()
