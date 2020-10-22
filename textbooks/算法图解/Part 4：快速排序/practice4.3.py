'''
Author: ZhXZhao
Date: 2020-10-22 16:09:20
LastEditors: ZhXZhao
LastEditTime: 2020-10-22 16:49:25
Description:
'''


def findmax(list):
    max = list[0]
    if len(list) == 1:
        return list[0]
    return max if max > findmax(list[1:]) else findmax(list[1:])


print(findmax([1, 10, 3, 4]))
