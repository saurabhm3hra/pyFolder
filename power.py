def is_power(a,b):
    if(a==b):
        return True
    if(a%b==0):
        if(is_power(a/b,b)):
            return True
        else:
            return False
    else:
        return False

print is_power(9,3)
