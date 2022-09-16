'''
This time no story, no theory. 
The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
#
#
#
def accum(s): 
    s = s.upper() # ABCD
    i=0
    new = str()
    for letter in s:
        new = new + letter + (letter.lower())*i + " "
        i += 1
    new = new.strip().replace(" ", "-")
    return new
#
#
#
def accum(s):
    msg = ""
    counter=0
    for letter in s:
        
        msg = msg + letter.upper() + (letter.lower() * counter)+"-"
        counter +=1
    return msg[:-1]
