'''
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
'''
#
#
#
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
#
#
#
def stray(arr):
    dict={}
    for element in arr:
        if element not in dict:
            dict[element] = 1
        else: dict[element] +=1
    for x, y in dict.items():
        if y==1: return x
#
#
#