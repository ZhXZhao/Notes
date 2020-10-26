'''
Author: ZhXZhao
Date: 2020-10-22 21:59:46
LastEditors: ZhXZhao
LastEditTime: 2020-10-24 15:54:30
Description:
'''

# 这个快速排序用了额外的数组空间，正确的做法应该是直接交换数组中的元素


def quicksort(list):
    if len(list) < 2:
        return list
    base = list[0]  # 简单的基准值选择，快排的效率和基准值的选择有很大的关系
    list1 = []
    list2 = []
    for i in list[1:]:
        if i <= base:
            list1.append(i)
        elif i > base:
            list2.append(i)
    # print(list)
    return quicksort(list1) + [base] + quicksort(list2)


# 正统快排，直接在原数组上进行元素的交换，无需额外的数组空间，但递归需要占用栈空间
# 从小到大排序
def quick_sort(list, low, high):
    if low >= high:
        return
    j = partition(list, low, high)
    quick_sort(list, low, j-1)
    quick_sort(list, j+1, high)

# 将小于基准值的元素交换到基准值左边，大于基准值的元素交换到基准值右边
# 注意：若选择的基准值为数组的最左边的元素，则需要先从数组的最右边开始查找小于基准值的元素
# 若选择的基准值为数组的最右边的元素，则需要先从数组的最左边开始查找大于基准值的元素
# 原因：当基准值为数组最左边的元素时，因为最后要将数组最左边的元素与指针停下来的地方交换
# 从数组最右边开始查找，会在小于基准值的地方停止下来，而若从数组最左边开始查找，指针有可能会停在大于基准值的地方。


def partition(list, low, high):
    pivot = list[low]
    i = low
    j = high
    while i != j:
        while list[j] >= pivot and i < j:
            j -= 1
        while list[i] <= pivot and i < j:
            i += 1
        list[i], list[j] = list[j], list[i]
    list[low], list[j] = list[j], list[low]
    return j


list = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
# print(quicksort(list))
quick_sort(list, 0, len(list)-1)
print(list)
