from functools import reduce, lru_cache
from operator import mul
# abaixo parametros pra aumentar o limite do número inteiro que vc fornecer
from sys import set_int_max_str_digits
set_int_max_str_digits(6400001)
#

def factorial_checks(func):
    def verify(number):
        if number<0: return('Não há numero negativo')
        if number==0: return 1
        else: return func(number)
    return verify
    



@factorial_checks
@lru_cache
def factorial_calculus (number:int):
    return(reduce(mul, range(1, number+1)))

print(factorial_calculus(int(input())))

    