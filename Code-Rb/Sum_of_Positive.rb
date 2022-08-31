#INSTRUCTIONS
=begin
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.


=end
# Minha solução
#arr = [-9, 7, 100, -12, -23, 0]  #TESTE
#
def positive_sum(arr)
    # your code here
    soma = 0
    for item in arr
      if item >= 0
        soma = soma + item
      end
    end
    return soma
  end 

