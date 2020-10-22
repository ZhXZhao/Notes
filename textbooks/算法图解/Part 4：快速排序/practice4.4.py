'''
Author: ZhXZhao
Date: 2020-10-22 16:17:04
LastEditors: ZhXZhao
LastEditTime: 2020-10-22 22:02:48
Description:
'''


# def binary_search(list, item):
#     if len(list) != 0:
#         mid = len(list)//2
#         if item > list[mid]:
#             return binary_search(list[mid+1:], item)
#         elif item < list[mid]:
#             return binary_search(list[:mid], item)
#         elif item == list[mid]:
#             return list[mid]
#     else:
#         return None


def b_s(list, item, start=0, end=0):
    if start <= end:
        mid = (end-start) // 2 + start
        if item > list[mid]:
            return b_s(list, item, mid+1, end)
        elif item < list[mid]:
            return b_s(list, item, start, mid-1)
        elif item == list[mid]:
            return mid
    else:
        return None


list = [1, 2, 3, 4, 5]
# print(binary_search(list, -1))
print(b_s(list, 5, 0, 4))
# print(binary_search(list, -1))
