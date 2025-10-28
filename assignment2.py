"""
### Assignment 2
Prime numbers
Given a list of numbers that are integers, create a map() that shows whether each of the numbers is a perfect square.
"""

data = [76, 56, 20, 77, 42, 97, 83, 47] 

def ispsquare(n):
    if int(n**0.5) == n**0.5:
        return True
    else:
        return False
result = map(ispsquare, data)
print(list(result))
# expected output:  [False, False, False, False, False, False, False, False]

