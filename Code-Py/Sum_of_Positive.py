#INSTRUCTIONS
'''
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.


'''
# Minha solução
#arr = [-9, 7, 100, -12, -23, 0]  #TESTE
def positive_sum(arr):
    # Your code here
    soma = 0
    for item in arr:
        if item < 0:   # pode ser < ou <= ambas condições OK
            pass
        else:
            soma = soma + item
    return soma
#
#
# SOLUÇÕES ALTERNATIVAS
#
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
#
#
#
def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum
#    
#    
#    
def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))
#
#
#
def positive_sum(list):
    answer = 0
    for numbers in list: 
        if numbers > 0:
            answer += numbers
    return answer
#print(positive_sum(arr))  #TESTE