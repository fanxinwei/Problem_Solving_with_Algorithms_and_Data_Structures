class Stack():  #最右边是top
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if self.stack == []:
            return True
        else:
            False
    def push(self, item):
        self.stack.append(item)
        return self.stack
    def pop(self):
        m =self.stack.pop()
        return m
    def peek(self): #return the last one
        last_num = len(self.stack) - 1
        return self.stack[last_num]
    def size(self):
        num = len(self.stack)
        return num
    # def reverse(self):
    #     new_list = []
    #     i = len(self.stack) - 1
    #     while i >= 0:
    #         m = self.stack[i]
    #         new_list.append(m)
    #         i = i - 1
    #     return new_list
