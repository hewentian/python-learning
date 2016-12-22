# －*- coding: utf-8 -*-
print ord('A')
print chr(65)
print u'中文'
print u'中'

print u'ABC'.encode("utf-8")
print u'中文'.encode("utf-8")

print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print 'Hello, %s' % 'world'
print 'Hi, %s, you have $%d' % ('Michael', 1000000)

print '%2d-%02d' % (3, 1)
print '%.2f' % 3.1415926
print 'Age: %s. Gender: %s' % (25, True)
print u'Hi, %s' % u'Michael'
print 'growth rate: %d %%' % 7
