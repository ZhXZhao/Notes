'''
Author: ZhXZhao
Date: 2020-11-20 10:20:40
LastEditors: ZhXZhao
LastEditTime: 2021-03-26 16:15:59
Description:
'''


def insertsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


arr = [1, 3, 2, 4]
insertsort(arr)
print(arr)
