from Stack_function import Stack

def dicimal_to_binary(k):
    mystack = Stack()
    new_string = ''
    if k == 1:    #排除0、1的二进制
        return 1
    if k == 0:
        return 0
    else:
        while k != 0:
            remainder = k % 2 # 余数
            mystack.push(remainder)
            k = k // 2  #除数
    while not mystack.is_empty():
        index = str(mystack.pop())
        new_string = new_string + index   #字符串可以通过加号连接
    return new_string

print(dicimal_to_binary(20))



