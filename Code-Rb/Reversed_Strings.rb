# Instructions
=begin
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

=end

# Solutions
# Abaixo coloquei algumas possibilidades de soluções

def solution(str)
    str = str.reverse
end
  
  
def solution(str)
    return str.reverse  # não afeta a string original, entrega uma cópia invertida
end
  
  
def solution(str)
    return str.reverse!  #reverse! afeta a string original 
end

# Sample Tests
=begin
#
describe "Fixed tests" do
    it "should pass fixed tests" do
      Test.assert_equals(solution('world'), 'dlrow')
      Test.assert_equals(solution('hello'), 'olleh')
      Test.assert_equals(solution(''), '')
      Test.assert_equals(solution('h'), 'h')
    end
end
#
=end
