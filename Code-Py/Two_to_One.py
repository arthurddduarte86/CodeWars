'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''
#
#
#
def longest(a1, a2):
    dic_char={}
    for char in a1:
        if char not in dic_char: dic_char[char]=char
        else: pass
    for char in a2:
        if char not in dic_char: dic_char[char]=char
        else: pass
    lista = list(dic_char.values())
    lista.sort()
    return ''.join(lista)
#
#
#
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
#
#