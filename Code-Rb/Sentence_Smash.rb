=begin
# Instructions
Sentence Smash

Write a function that takes an array of words and smashes them 
together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, 
but you should add spaces between each word. 
Be careful, there shouldn't be a space at the beginning 
or the end of the sentence!

=end
# Solutions
# Abaixo coloquei algumas possibilidades de soluções

# Smash Words
def smash(words)
    return words.join(" ")
  end
  
  
def smash(words)
    words.join (' ')
end
  

def smash(words)
    words.join ' '
end
  
  
def smash(words)
    words * ' '
end
  

def smash(words)
    return "" if words.empty?
    words.join(" ")
end
  
  
=begin
# Abaixo código para testes
Sample Tests

describe "Basic Tests" do
  it "should pass basic tests" do
    Test.assert_equals(smash([]), "")
    Test.assert_equals(smash(["hello"]), "hello")
    Test.assert_equals(smash(["hello", "world"]), "hello world")
  end
end

=end

  