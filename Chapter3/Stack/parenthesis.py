from Stack_function import Stack

def cheek_balance(list):
    mystack = Stack() # 初始化一个stack的空间
    index = 0
    num = len(list)
    while index < num and index >= 0:
        i = list[index] #从list中取出一个需要判断的符号
        if i == '(': #push进stack
            mystack.push(i)
        if i == ')' and mystack.is_empty():
            return 'sorry, it is not balance'
        if i == ')':
            mystack.pop()

        index = index + 1

    if mystack.is_empty() == True:
        return 'perfect'
    else:
        return 'sorry'

print(cheek_balance('('))
print(cheek_balance('()'))
print(cheek_balance('())'))


