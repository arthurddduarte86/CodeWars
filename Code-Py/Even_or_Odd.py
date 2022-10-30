'''
Create a function that takes an integer as an argument and returns "Even" 
for even numbers or "Odd" for odd numbers.
'''
def even_or_odd(number): return "Even" if number%2==0 else "Odd"

# outra forma
def even_or_odd(number): return ["Even", "Odd"][number % 2]

# outra forma
even_or_odd = lambda number: "Odd" if number % 2 else "Even"