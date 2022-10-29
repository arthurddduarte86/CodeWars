## *args

def mult(x, y):
    return x*y

print("função mult: ", mult(4, 5))  # resultado 20

def mult2(*args):
    result=1
    for number in args:
        result *= number
    print("função mult2: ", result)

mult2(2, 3, 4, 5, 6, 7)


## **kwargs
## Retorna como dicionário.

def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(Nome="Arthur", Idade=36, Vivo=True)

##
##
#
def print_values(**kwargs):
    for key, value in kwargs.items():
        print(f"The value of {key} is {value}.")

print_values(
    Nome='Arthur',
    Idade=36,
    Nacionalidade='Brasileiro',
    Vivo=True,
    Peso=66,
    Altura=1.75    
)

#
#
##  Using *args and **kwargs in Function Calls

def some_args(arg01, arg02, arg03):
    print(f"arg01 -> {arg01} _ arg02 -> {arg02} _ arg03 -> {arg03}")
args = ("Arthur", "Pedro", "João")
some_args(*args)

#
def some_args02(arg01, arg02, arg03):
    print(f"arg01 -> {arg01} _ arg02 -> {arg02} _ arg03 -> {arg03}")
my_lista=(100, [200, 300, 400, {'ID': 123, 'Name':"Eu"}])
some_args02(True, *my_lista)
    
#
#
def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_01:", kwarg_1)
    print("kwarg_02:", kwarg_2)
    print("kwarg_03:", kwarg_3)

kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_kwargs(**kwargs)



