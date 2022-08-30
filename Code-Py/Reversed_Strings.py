# Instructions
'''
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

'''

# Solutions
# Abaixo coloquei algumas possibilidades de soluções

def solution(string):
    string = string[::-1]
    return  string

def solution(string):
    return string[::-1]
       
def solution(string):
    string = "".join(reversed(string))
    return string
    
def solution(string):
    string = list(string)
    string.reverse()
    return "".join(string)


# Sample Tests
'''
import codewars_test as test
from solution import solution

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solution('world'), 'dlrow')
        test.assert_equals(solution('hello'), 'olleh')
        test.assert_equals(solution(''), '')
        test.assert_equals(solution('h'), 'h')
        

'''