'''
Author: ZhXZhao
Date: 2020-10-22 21:59:46
LastEditors: ZhXZhao
LastEditTime: 2020-10-22 22:26:46
Description:
'''


def quicksort(list):
    if len(list) < 2:
        return list
    base = list[0]
    list1 = []
    list2 = []
    for i in list[1:]:
        if i < base:
            list1.append(i)
        elif i > base:
            list2.append(i)
    # print(list)
    return quicksort(list1) + [base] + quicksort(list2)


list = [10, 5, 2, 3]
print(quicksort(list))
