from Stack_function import Stack

def reverse(list):
    mystack = Stack()
    new_string =''
    for i in list:
        mystack.push(i)

    while not mystack.is_empty():
        index = mystack.pop()
        new_string = new_string + index
    return new_string
