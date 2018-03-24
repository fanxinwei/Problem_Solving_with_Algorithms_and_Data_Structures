### bad algorithm-find the smallest number O(n^2) ####
import time
from random import randrange

def find_min(list):
    n = len(list)
    for i in range(n):
        for j in range(n):
            if list[j] < list[i]:
                continue
    print('the smallest number is', list[i])

def mainA():
    list = [5, 4, 3, 2, 1, 0]
    find_min(list)

def mainB():
    for listsize in range(1000, 10001, 1000):
        list = [randrange(100000000) for x in range(listsize)]
        start = time.time()
        find_min(list)
        end= time.time()
        print ("size: %d time: %f " % (listsize, end-start))

mainB()


#### good algorithm O(n) ######
import time
from random import randrange
def Find_Min(list):
    flag = list[0]
    for i in list:      ##python很高级，可以直接循环list！
        if i < flag:
            flag = i
    return flag

def mainA():
    list = [5, 4, 3, 2, 1, 0]
    print(Find_Min(list))

def mainB():
    for listsize in range(1000, 10001, 1000):
        list = [randrange(100000000) for x in range(listsize)]
        start = time.time()
        Find_Min(list)
        end= time.time()
        print ("size: %d time: %f " % (listsize, end-start))
mainB()