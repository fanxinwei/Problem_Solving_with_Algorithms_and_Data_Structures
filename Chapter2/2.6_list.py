
import time

def test1():  # for + concatenation
   l = []
   for i in range(1000):
       l = l + [i]
   return l


def test2():   # for + append
   l = []
   for i in range(1000):
       l.append(i)


def test3():
   l = [i for i in range(1000)]


def test4():
   l = list(range(1000))


start = time.time()
test1()
end = time.time()
print("%10.7f" %(end-start))  # %10.(7)小数点后面有几位

start =time.time()
test2()
end = time.time()
print("%10.7f" %(end-start))


start =time.time()
test3()
end = time.time()
print("%10.7f" %(end-start))

start =time.time()
test4()
end = time.time()
print("%10.7f" %(end-start))