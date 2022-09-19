<<<<<<< HEAD
'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''
#
#
def square_digits(num): 
    result = "".join(f'{int(value)**2}' for value in str(num))
    return int(result)
# First of all, need to convert (num) to string, because integer values
# are not iterable in python.

=======
'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''
#
#
def square_digits(num): 
    result = "".join(f'{int(value)**2}' for value in str(num))
    return int(result)
# First of all, need to convert (num) to string, because integer values
# are not iterable in python.

>>>>>>> refs/remotes/origin/main
