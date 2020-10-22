'''
Author: ZhXZhao
Date: 2020-10-22 15:16:44
LastEditors: ZhXZhao
LastEditTime: 2020-10-22 15:31:27
Description:
'''


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


print(gcd(1680, 640))
