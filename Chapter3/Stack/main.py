from Stack_function import Stack  ##从相同工程下的Stack_function.py取出Stack class的定义
s = Stack()
print(s.is_empty())
print(s.push(4))
print(s.peek())
print(s.push(5))
print(s.push('dog'))
#print(s.pop())
print(s.peek())
print(s.size())
print(s.reverse())

