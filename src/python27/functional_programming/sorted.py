# -*- coding: utf-8 -*-
print sorted([36, 5, 12, 9, 21])


def reversed_cmp(x, y):
    if x > y:
        return -1
    elif x == y:
        return 0
    else:
        return 1

print sorted([36, 5, 12, 9, 21], reversed_cmp)

print sorted(['bob', 'about', 'Zoo', 'Credit'])


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 > u2:
        return 1
    elif u1 < u2:
        return -1
    else:
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
