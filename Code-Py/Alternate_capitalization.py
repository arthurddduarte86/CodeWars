'''

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity



'''


def capitalize(s):
    message1 = "".join(char.upper() if not ind%2 else char.lower() for ind, char in enumerate(s))
    message2 = "".join(char.upper() if ind%2 else char.lower() for ind, char in enumerate(s))
    return [message1, message2]

# eu poderia ter feito,  message2 = message1.swapcase()

