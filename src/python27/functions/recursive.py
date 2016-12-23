# -*- coding: utf-8 -*-
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)
# fact(1000)


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num - 1, num * product)


print fact2(5)
# print fact2(1000)
