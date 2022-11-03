import timeit

# testando o desafio codewars usando o código pra ver o tempo de execução 
# para o array que eu criei.

mysetup=''
code ='''
i=1
arr=[]
j=1
while i<10_0000:
    while j < i*2:
        arr.append(j)
        j+=0.01
    i+=1
   
def find_uniq(arr):
    dic_numbers={}
    for numero in arr:
        if numero not in dic_numbers: dic_numbers[numero]=1
        else: dic_numbers[numero]+=1
    for x, y in dic_numbers.items():
        if y ==1: return x

print(find_uniq(arr))
'''
exec_time = timeit.timeit(stmt=code,
                        setup=mysetup,
                        number=1)*1000
print(f'{exec_time:.03f}ms')
