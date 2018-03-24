# test = [1,2,3]
# list = '(())))'
# list2 ='()('
# # def hah(list):
# #     print (len(list))
# #     for i in list:
# #         if i == '(':
# #             return 'good'
# #
# # print(hah(list))
# print(test.insert(0, 9))
import random
total = 0
for i in range(180):
    k = random.randint(1,180)
    if k == 180:
        total = total + 1
print(total)

