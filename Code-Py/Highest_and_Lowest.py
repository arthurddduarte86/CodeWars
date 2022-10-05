'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''
#
#
#
import numpy as np
def high_and_low(numbers):
    number = numbers.split() #split the string at first
    result = np.sort(np.array(number).astype(int)) # convert the list of string to list of integer and sort 
    return (f"{result[-1]} {result[0]}") #return the result filtered 
#
#
#
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])
#
#
#
def high_and_low(numbers):
    a = list(map(int, numbers.split()))
    return "{} {}".format(max(a), min(a))
#    
#
#
high_and_low=lambda x:max(x.split(' '),key=int)+' '+min(x.split(' '),key=int)
#
#
#