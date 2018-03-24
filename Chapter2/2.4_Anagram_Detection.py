

##### O(n^2) ####
def anagram_solution1(listA, listB):
    if len(listA) == len(listB):   # compare the length
        for i in listA:
            for j in listB:
                if i != j:
                    flag = False
                    continue
                else:
                    flag = True
                    break
            if flag == True:
                continue
            else:
                return False
        if flag == True:
            return True
    else:
        return False

list1 ='abcd'
list2 ='cbaf'
print (anagram_detection(list1,list2))


#### string alphabetically, from a to z O(n)###

def anagram_solution2(s1,s2):
    alist1 = list(s1)    #转化成list才能进行字母排序
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    flag = 0
    if len(alist1) != len(alist2):
        return False
    while flag < len(alist1):
        if alist1[flag] == alist2[flag]:
            flag = flag + 1
        else:
            return False
    return True

print(anagram_solution2('abcde','edcba'))
