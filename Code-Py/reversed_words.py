#Complete the solution so that it reverses all of the words
#within the string passed in.

#Example(Input --> Output):

#"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
#
#
def reverse_words(s):
    s = s.split(" ")
    return " ".join(s[len(s)-1::-1])
#
#
#
def reverse_words(s):
    return " ".join(reversed(s.split()))
#
#
#    
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])