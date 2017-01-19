# -*- coding: utf-8 -*-
import os

# windows下请注释如下代码, windows没有fork函数
#print 'Process (%s) start...' % os.getpid()
#pid = os.fork()
#if pid == 0:
#    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
#else:
#    print 'I (%s) just created a child process (%s).' % (os.getppid(), pid)

from multiprocessing import Process


def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
