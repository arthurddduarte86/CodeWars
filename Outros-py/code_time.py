# Tutorial from
# https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/
# https://www.guru99.com/timeit-python-examples.html
#
# importing the required module
import timeit
from functools import reduce, cache
from operator import mul
# abaixo parametros pra aumentar o limite do número inteiro que vc fornecer
from sys import set_int_max_str_digits
set_int_max_str_digits(100_000_000)
#
# =========================================================================
# code snippet to be executed only once
# before the stmt parameter in timeit
mysetup = '''from functools import reduce, lru_cache
from operator import mul
#códigos que devem ser executados antes do   stmt'''
# ========================================================================= 
# code snippet whose execution time
# is to be measured
mycode = '''
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

factorial_calculus(100_000)
'''
# ========================================================================= 
# timeit statement
exec_time = timeit.timeit(stmt=mycode,
                          setup=mysetup,
                          number=2) * 10**3
print(f"The time of execution of above program is : {exec_time:.03f}ms")
