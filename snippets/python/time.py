import time

start = time.time()
print "hello"
end = time.time()
print end - start



# decorateur

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print '%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000)
        return result

    return timed


# -*- coding: utf-8 -*-
# python
# example of using timeit.timeit
# testing the speed of a function that takes one argument

mydata = 5

def f1(x):
    return x+1

import timeit

print timeit.timeit("f1(mydata)", setup = "from __main__ import f1, mydata", number=1)