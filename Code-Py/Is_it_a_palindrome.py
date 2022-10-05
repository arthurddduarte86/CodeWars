'''
Write a function that checks if a given string (case insensitive) is a palindrome.
'''
#
#
#
def is_palindrome(s):
    len_s =len(s)
    reversed_str = ""
    for index in range(len_s - 1, -1, -1):
        reversed_str += s[index].lower()
    return True if reversed_str == s.lower() else False
#
#
#
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
#
#
#