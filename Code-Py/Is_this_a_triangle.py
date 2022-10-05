'''
ESTE KATA TEM PROBLEMAS.. NÃO FOI EXPLICADO DIREITO, NÃO FIZ, APENAS PEGUEI A SOLUÇÃO!!!

Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.


'''
#
#
#
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
#
#
#
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
#
#
#