'''
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''
#
#
def bmi(weight, height): 
    if (weight/(height**2)) <= 18.5: return "Underweight"
    if (weight/(height**2)) <= 25.0: return "Normal"
    if (weight/(height**2)) <= 30.0: return "Overweight"
    else: return "Obese"
#    
#
# 
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
#    
#    
#    
bmi = lambda w,h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5<b) + (25<b) + (30<b)])()
#
#