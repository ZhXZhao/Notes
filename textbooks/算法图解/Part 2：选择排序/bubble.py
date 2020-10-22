'''
Author: ZhXZhao
Date: 2020-10-20 16:30:00
LastEditors: ZhXZhao
LastEditTime: 2020-10-20 16:34:16
Description:
'''


def bubble(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp


mylist = [9, 10, 2, 3, 1]
bubble(mylist)
print(mylist)
