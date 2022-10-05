'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''
#
#
#
def count(string):
    count = {}
    for x in string:
        if x not in count: count[x]=1
        else: count[x]+=1
    return count
# created dictionar to store the format letter:quantity
#
#
from collections import Counter

def count(string):
    return Counter(string)
#
#
#