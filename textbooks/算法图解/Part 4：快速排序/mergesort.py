'''
Author: ZhXZhao
Date: 2020-10-24 15:54:58
LastEditors: ZhXZhao
LastEditTime: 2020-10-24 16:21:35
Description:
'''
# 归并排序
# 将数组拆分成2半递归进行排序，直到数组不再可分割，然后将拆分出来的2半按顺序合并后返回

def mergesort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])
    return merge(left, right)


def merge(list1, list2):
    temp = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            temp.append(list1[i])
            i += 1
        elif list2[j] <= list1[i]:
            temp.append(list2[j])
            j += 1
    while i < len(list1):
        temp.append(list1[i])
        i += 1
    while j < len(list2):
        temp.append(list2[j])
        j += 1
    return temp


list = [6, 1, 2, 5, 4, 3, 9, 7, 10, 8]
print(mergesort(list))
