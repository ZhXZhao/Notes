'''
Author: ZhXZhao
Date: 2020-10-22 15:31:13
LastEditors: ZhXZhao
LastEditTime: 2020-10-22 15:31:40
Description:
'''


def mysum(arr):
    return 0 if len(arr) == 0 else arr[0] + mysum(arr[1:])


print(mysum([1, 2, 3, 4]))
