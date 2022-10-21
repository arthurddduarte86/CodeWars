'''
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

'''
# Da primeira vez não consegui, peguei solução, tempos depois consegui sozinho
# Link para regra matemática, https://mundoeducacao.uol.com.br/matematica/condicao-existencia-um-triangulo.htm
#
#
def is_triangle(a, b, c):

    if (abs(b-c) < a < (b+c)) or (abs(a-c) < b < (a+c)) or (abs(a-b) < c < (a+b)): return True
    else: return False
#
#
#
