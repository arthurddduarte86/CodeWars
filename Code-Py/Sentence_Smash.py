'''
# Instructions
Sentence Smash

Write a function that takes an array of words and smashes them 
together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, 
but you should add spaces between each word. 
Be careful, there shouldn't be a space at the beginning 
or the end of the sentence!

'''
# Solutions
# Abaixo coloquei algumas possibilidades de soluções


def smash(words):
    frase = (" ".join(words))
    return frase

    
def smash(words):
   return " ".join(words)

   
def smash(words):
    return ' '.join(words).strip()

    
def smash(words):
    str1 =" ".join(words)
    return(str1) 

###
# Abaixo código para testes
'''
Sample Tests

import codewars_test as test
from solution import smash

@test.describe("smash")
def _():
    @test.it("Should return empty string for empty array.")
    def _():
        test.assert_equals(smash([]), "")
        
    @test.it("One word example should return the word.")
    def _():
        test.assert_equals(smash(["hello"]), "hello")
        
    @test.it("Multiple words should be separated by spaces.")
    def _():
        test.assert_equals(smash(["hello", "world"]), "hello world")
        test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
        test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")


'''



