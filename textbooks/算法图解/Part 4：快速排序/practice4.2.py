'''
Author: ZhXZhao
Date: 2020-10-22 15:31:49
LastEditors: ZhXZhao
LastEditTime: 2020-10-22 16:12:36
Description:
'''


def count_list(list):
    if len(list) == 0:
        return 0
    list.pop()
    return 1 + count_list(list)


print(count_list([1, 2, 3, 4]))
