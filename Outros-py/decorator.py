# ESTUDO SOBRE DECORATOR

def check(func):
    def inside(a, b):
        if b == 0:
            print("Não é possível divisão por 0")
            
        else: func(a, b)
    return inside



@check
def div(a, b):
    print(a / b)

# O DECORATOR é o mesmo que a linha abaixo
#div = check(div)
#
#
div(10, 1)