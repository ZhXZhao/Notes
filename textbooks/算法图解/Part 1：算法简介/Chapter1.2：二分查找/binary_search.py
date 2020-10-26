'''
Author: ZhXZhao
Date: 2020-10-20 15:22:55
LastEditors: ZhXZhao
LastEditTime: 2020-10-24 16:30:10
Description:
'''


def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None


mylist = [1, 3, 5, 6, 9]
print(binary_search(mylist, 6))
print(binary_search(mylist, -1))
