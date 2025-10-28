"""
### Assignment 1
Convert to Fahrenheit
Given a list of numbers that are in degrees Celsius, create a map() that returns a list of all the numbers converted to degrees Fahrenheight
"""

data = [0, 10, 20.1, 34.5]
farenheit = map(lambda x: (x*(9/5)) + 32, data)
print(list(farenheit))
# expected output:  [32.0, 50.0, 68.18, 94.1]