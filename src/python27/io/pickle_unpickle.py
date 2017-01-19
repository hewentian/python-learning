# -*- coding: utf-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d)

f = open('d:\\dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('d:\\dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dic(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 80)
print json.dumps(s, default=student2dic)
print json.dumps(s, default=lambda obj: obj.__dict__)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str, object_hook=dict2student)
