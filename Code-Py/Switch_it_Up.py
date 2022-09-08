'''
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
'''
#
#
def switch_it_up(number):
    switch = {
        1:'One',
        2:"Two",
        3:"Three",
        4:"Four",
        5:'Five',
        6:'Six',
        7:'Seven',
        8:'Eight',
        9:'Nine',
        0:'Zero',
        } 
    return switch.get(number)
#
#
#
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
#
#
#
def switch_it_up(number):
    number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    return number_converter[number]
#    
#    
# 