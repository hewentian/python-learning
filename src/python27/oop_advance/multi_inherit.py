# -*- coding: utf-8 -*-


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# all kind of animal
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print 'Running...'


class Flyable(object):
    def fly(self):
        print 'Flying...'


class Dog2(Mammal, Runnable):
    pass


class Bat2(Mammal, Flyable):
    pass
