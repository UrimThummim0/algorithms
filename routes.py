"""
    Starting in the top left corner of a 2x2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20x20 grid?
"""

from math import factorial

def routes(n):
    return factorial(2*n) // (factorial(n)**2)

print(routes(20))
