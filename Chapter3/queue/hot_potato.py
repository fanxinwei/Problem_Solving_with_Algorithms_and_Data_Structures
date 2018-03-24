from queue_structure import Queue

def hot_potato(List, num):
    queue = Queue() # 初始化一个排队
    for i in List:
        queue.enqueue(i)
    print(queue.print_queue()) #放入queue，已将考虑了bill在最前面

    while queue.size() > 1: #最后只剩下一个人
        for k in range(num):  # k = 1,2,3,4,5,6,7
            name = queue.dequeue()
            queue.enqueue(name)
        queue.dequeue() #达到7次后删除第一个

    return queue.print_queue()

Namelist = ["Bill","David","Susan","Jane","Kent","Brad"]
print (hot_potato(Namelist, 7))