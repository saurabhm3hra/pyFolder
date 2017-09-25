import math

def area(n, s):
    """
    returns area of polynomial with n sides and length s
    """
    return (0.25*n*s**2)/(math.tan(180/n))

def perimeter(n, s):
    """
    returns perimeter of polynomial with n sides and length s
    """
    return n*s

def polysum(n, s):
    """
    returns sum of the area and square of the perimeter of the regular polygon with n sides and length s
    """
    summ = area(n,s) + perimeter(n,s)
    return round(summ, 4)