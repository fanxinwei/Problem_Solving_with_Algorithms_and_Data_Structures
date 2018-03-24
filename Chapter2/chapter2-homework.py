##### q1 #####
from timeit import Timer

def Index():
    l = list(range(1000))
    for i in range(1000):
        l[i]


def POP0():
    l = list(range(1000))
    for i in range(1000):
        l.pop(0)


t1 = Timer("Index()", "from __main__ import Index")
print("list index operation:", t1.timeit(number=1000), "milliseconds")  ## number:重复运行1000次的总计时间

t2 = Timer("POP0()", "from __main__ import POP0")
print("list pop0 operation:", t2.timeit(number=1000), "milliseconds")

### q2 ####

def dic_get():
    d = dict(zip(list(range(1000)), list(range(4000, 5000))))
    for i in range(1000):
        m = d[i]


def dic_set():
    d = dict(zip(list(range(1000)), list(range(4000, 5000))))
    for i in range(1000):
        d[i] = 1

def dic_iter():
    d = dict(zip(list(range(1000)), list(range(4000, 5000))))
    for i in range(1000):
        for x in d:
            pass


t4 = Timer("dic_get()", "from __main__ import dic_get")
print("dic get items:", t4.timeit(number=1000), "milliseconds")  ## number:重复运行1000次的总计时间

t5 = Timer("dic_get()", "from __main__ import dic_get")
print("dic set items:", t5.timeit(number=1000), "milliseconds")

t6 = Timer("dic_get()", "from __main__ import dic_get")
print("dic iteration:", t6.timeit(number=1000), "milliseconds")









