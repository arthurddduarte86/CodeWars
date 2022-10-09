'''
In this Kata we are passing a number (n) into a function.

Your code will determine if the number passed is even (or not).

The function needs to return either a true or false.

Numbers may be positive or negative, integers or floats.

Floats with decimal part non equal to zero are considered UNeven for this kata.
'''
#
#
#
def is_even(n): 
    return True if n % 2 == 0 else False
#
#
#
def is_even(n):

#a modulos will return the whole number remainder of a division

#using the modulos sign with 2 and another number will only return 0 and 1 

#if the remainder of n and 2 is equal to 1 the number will be odd
   
    if (n % 2) == 1:
      return False
      
    #if the remainder of n and 2 is equal to 0 the number will be even
    
    elif (n % 2) == 0:
      return True 
      
    #if n is not an integer (i.e a float) return False
    
    elif (n) != int: 
      return False 
      
    #Done ( ಠ ͜ʖಠ)
#
#
#