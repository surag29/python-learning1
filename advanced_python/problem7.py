from functools import reduce

def divisible5(n):
    if(n%5 ==0):
        return True
    return False
a = [2,34,55,66,66,45,66,54,64]


f = list(filter(divisible5,a))
print(f)