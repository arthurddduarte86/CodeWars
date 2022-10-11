'''
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
'''
#
#
#
def quarter_of(month):
    if month <= 3:
        return 1
    if month > 3 and month <= 6:
        return 2
    if month > 6 and month <= 9:
        return 3
    if month > 9:
        return 4
#
#
#
def quarter_of(month): 
    quarter = {
        '1':1,
        '2':1,
        '3':1,
        '4':2,
        '5':2,
        '6':2,
        '7':3,
        '8':3,
        '9':3,
        '10':4,
        '11':4,
        '12':4
    }
    return quarter.get(f"{month}")
#
#
#
def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
#
#
#
def quarter_of(n):
    return (n + 2) // 3
#
#
