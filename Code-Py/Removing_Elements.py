'''

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!

'''
# MINHA SOLUÇÃO MALUCA
def remove_every_other(my_list):
    x=0
    newarray=[]
    while x < len(my_list):
        if x % 2 == 0: newarray.append(my_list[x])
        x+=1
    return newarray
#
#
# Outras possiveis soluções
#
#
def remove_every_other(my_list):
    return my_list[::2]
#
#    
def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r
#
#    
def remove_every_other(my_list):
    return [v for c,v in enumerate(my_list) if not c%2]
#
#    
def remove_every_other(my_list):
    del my_list[1::2]
    return my_list
#
#    
remove_every_other = lambda m: m[::2]
#
#
