'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
'''
# Minha solução final para evitar time-out
def find_uniq(arr):
    dic_numbers={}
    for numero in arr:
        if numero not in dic_numbers: dic_numbers[numero]=1
        else: dic_numbers[numero]+=1
    for x, y in dic_numbers.items():
        if y ==1: return x
#        
#
#
# Minha solução inicial mas que caiu no problema de time-out
def find_uniq(arr):
    for n in arr:
        if arr.count(n) == 1: return n
        else: pass 
#
#
#Solução que um usuário no discord me deu
def find_uniq(arr):
    a = [n for n in arr if arr.count(n)==1]
    return a[0]
#
#
# minha solução
def find_uniq(arr):
    n=0
    lista_ban=[]
    while n < len(arr):
        if arr.count(arr[n])!=1 and arr[n] not in lista_ban:
            lista_ban.append(arr[n])
        elif arr[n] in lista_ban: pass
        else: return arr[n]
        n+=1
#
#
# Soluções que o pessoal no server do discord me deu e a última solução 
# achei no Codewars
import pandas as pd
def find_uniq(arr):
    a = pd.DataFrame(arr)
    b = [a[0].value_counts() == 1]
    b = tuple(b)
    c = b[0].index.values
    n=c[b]
    return n
#
#
#
def group_by_occurrence(numbers):
    ocurrences = {}

    for number in numbers:
        if number in ocurrences:
            total = ocurrences[number]
            ocurrences[number] = total + 1
        else:
            ocurrences[number] = 1

    return ocurrences
#
#
#
def find_uniq_in_ocurrences(ocurrences):
    for number, total in ocurrences.items():
        if total == 1:
            return number

def find_uniq(arr):
    number_ocurrences = group_by_occurrence(arr)

    return find_uniq_in_ocurrences(number_ocurrences)    
#
#
# Solução de alguém no codewars
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
#
#