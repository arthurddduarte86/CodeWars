'''
You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
'''
#
#
#
def two_sort(array):
    array = sorted(array)
    message=""
    for char in array[0]:
        message+= char+"***" #vai adicionar *** também no final da string
    return message[:-3]
#
#
#
def two_sort(arr):
    return '***'.join(sorted(arr)[0])
#
#
#
def two_sort(lst):
    return '***'.join(min(lst))
#
#
#
two_sort = lambda a: "***".join(sorted(a)[0])
#
#