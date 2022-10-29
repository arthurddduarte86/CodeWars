# Estudo sobre algoritmo do cáculo de fatorial
# importar as bibliotecas abaixo
from functools import reduce, lru_cache
from operator import mul
#


# método normal e bastante comum, passei argumentos com atributos na função
def factorial(number:int, factorial=1):
    if number == 0: return 1
    else: 
        for n in range(1, number+1):
            factorial *= n
    return factorial
# chamando a função
print(factorial(4))


# Segunda forma de criar este algoritmo, usando bibliotecas importadas
def new_factorial(number:int):
    if number == 0: return 1
    return reduce(mul, range(1, number+1))
# chamando a função
print(new_factorial(4)) 


# Terceira forma, bastante interessante pois usa um buffer pra armazenar os valores
@lru_cache
def factorial_with_cache(number:int):
    if number == 0: return 1
    return reduce(mul, range(1, number+1))

# chamando a função
# detalhe: chamando fatorial de 6 pela primeira vez, sem valor armazenado anteriormente
print(factorial_with_cache(6))
# detalhe: para fatorial de 7, faz apenas uma nova chamada, o valor de 6! já está armazenado
#print(factorial_with_cache(7))
#detalhe para fatorial de 5, apenas olhou os resultados já armazenados anteriormente
#print(factorial_with_cache(5))
