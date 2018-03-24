# the data structure of queue
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.insert(0, item)
    def dequeue(self):
        return self.queue.pop()
    def  is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
        #return self.queue == []
    def size(self):
        return len(self.queue)
    def print_queue(self):
        return self.queue



#myqueue = Queue()
#print(myqueue.enqueue(1))
#print(myqueue.print_queue())
# print(myqueue.size())
# print(myqueue.is_empty())
# print(myqueue.dequeue())
