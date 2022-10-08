'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''
#
#
#
import math
def grow(arr):
    return math.prod(arr)
#
#
#
def grow(arr):
    res = 1
    i = 0
    while i < len(arr):
        res = res * arr[i]
        i += 1
    return res
#
#
#
def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product
#
#