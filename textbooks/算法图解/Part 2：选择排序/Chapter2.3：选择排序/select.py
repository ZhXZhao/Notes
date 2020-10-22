'''
Author: ZhXZhao
Date: 2020-10-20 17:06:58
LastEditors: ZhXZhao
LastEditTime: 2020-10-20 17:32:45
Description:
'''


def selectSort(arr):
    newArr = []
    for i in range(len(arr)):
        index = findindex(arr)
        newArr.append(arr.pop(index))
    return newArr


def findindex(arr):
    small = arr[0]
    smallindex = 0
    for i in range(len(arr)):
        if arr[i] < small:
            small = arr[i]
            smallindex = i
    return smallindex


mylist = [10, 4, 5, 8, 7]
print(selectSort(mylist))
